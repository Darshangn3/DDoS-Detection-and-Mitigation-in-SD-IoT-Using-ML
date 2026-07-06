from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, CONFIG_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib import hub
from ryu.lib.packet import packet, ethernet, ipv4, tcp, udp, icmp

import pandas as pd
import joblib
from collections import defaultdict


class DDoSMLController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(DDoSMLController, self).__init__(*args, **kwargs)

        # Load ML model
        self.model = joblib.load("ddos_rf_model.pkl")
        self.logger.info("ML model loaded")

        # Window counters
        self.packet_count = 0
        self.total_bytes = 0
        self.syn_count = 0
        self.ack_count = 0
        self.tcp_packets = 0
        self.udp_packets = 0

        self.src_ips = set()
        self.dst_ips = set()

        # Per-IP counters
        self.ip_syn_counter = defaultdict(int)

        self.datapaths = {}

        # 1-second monitoring window
        self.monitor_thread = hub.spawn(self.monitor)

    # --------------------------------------------------
    # Switch connected
    # --------------------------------------------------
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        dp = ev.msg.datapath
        ofp = dp.ofproto
        parser = dp.ofproto_parser

        self.datapaths[dp.id] = dp

        # ✅ ARP
        self.add_flow(dp, 20,
                      parser.OFPMatch(eth_type=0x0806),
                      [parser.OFPActionOutput(ofp.OFPP_FLOOD)])

        # ✅ ICMP
        self.add_flow(dp, 5,
                      parser.OFPMatch(eth_type=0x0800, ip_proto=1),
                      [parser.OFPActionOutput(ofp.OFPP_FLOOD)])

        # 🔥 TCP → Controller
        self.add_flow(dp, 10,
                      parser.OFPMatch(eth_type=0x0800, ip_proto=6),
                      [parser.OFPActionOutput(ofp.OFPP_CONTROLLER,
                                              ofp.OFPCML_NO_BUFFER)])

        # Table-miss
        self.add_flow(dp, 0,
                      parser.OFPMatch(),
                      [parser.OFPActionOutput(ofp.OFPP_CONTROLLER,
                                              ofp.OFPCML_NO_BUFFER)])

        self.logger.info("ARP + ICMP allowed, TCP redirected to controller")

    def add_flow(self, dp, priority, match, actions, idle_timeout=0):
        parser = dp.ofproto_parser
        ofp = dp.ofproto

        inst = [parser.OFPInstructionActions(
            ofp.OFPIT_APPLY_ACTIONS, actions)]

        mod = parser.OFPFlowMod(
            datapath=dp,
            priority=priority,
            match=match,
            instructions=inst,
            idle_timeout=idle_timeout
        )
        dp.send_msg(mod)

    # --------------------------------------------------
    # Packet-In
    # --------------------------------------------------
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        pkt = packet.Packet(msg.data)

        eth = pkt.get_protocol(ethernet.ethernet)
        if eth.ethertype != 0x0800:
            return

        if pkt.get_protocol(icmp.icmp):
            return

        ip_pkt = pkt.get_protocol(ipv4.ipv4)
        tcp_pkt = pkt.get_protocol(tcp.tcp)

        self.packet_count += 1
        self.total_bytes += msg.total_len
        self.src_ips.add(ip_pkt.src)
        self.dst_ips.add(ip_pkt.dst)

        if tcp_pkt:
            self.tcp_packets += 1
            if tcp_pkt.bits & tcp.TCP_SYN:
                self.syn_count += 1
                self.ip_syn_counter[ip_pkt.src] += 1

    # --------------------------------------------------
    # Monitor loop
    # --------------------------------------------------
    def monitor(self):
        while True:
            hub.sleep(1)
            self.detect_ddos()
            self.reset()

    # --------------------------------------------------
    # Detection
    # --------------------------------------------------
    def detect_ddos(self):
        if self.packet_count == 0:
            return

        features = pd.DataFrame([{
            "packet_count": self.packet_count,
            "total_bytes": self.total_bytes,
            "avg_packet_size": self.total_bytes / self.packet_count,
            "syn_count": self.syn_count,
            "ack_count": self.ack_count,
            "unique_src_ips": len(self.src_ips),
            "unique_dst_ips": len(self.dst_ips),
            "tcp_packets": self.tcp_packets,
            "udp_packets": self.udp_packets
        }])

        prediction = self.model.predict(features)[0]

        if prediction == 1 or self.syn_count > 50:
            print("\n🚨 DDoS ATTACK DETECTED 🚨")
            self.block_attackers()

    # --------------------------------------------------
    # Block attacker IPs
    # --------------------------------------------------
    def block_attackers(self):
        for ip, syns in self.ip_syn_counter.items():
            if syns > 50:
                print(f"[BLOCKED] {ip} | SYNs={syns}")
                for dp in self.datapaths.values():
                    self.add_flow(
                        dp, 100,
                        dp.ofproto_parser.OFPMatch(
                            eth_type=0x0800,
                            ipv4_src=ip
                        ),
                        [],
                        idle_timeout=20
                    )

    # --------------------------------------------------
    # Reset window
    # --------------------------------------------------
    def reset(self):
        self.packet_count = 0
        self.total_bytes = 0
        self.syn_count = 0
        self.ack_count = 0
        self.tcp_packets = 0
        self.udp_packets = 0
        self.src_ips.clear()
        self.dst_ips.clear()
        self.ip_syn_counter.clear()

