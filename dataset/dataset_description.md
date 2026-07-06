# Dataset Description

The dataset used in this project consists of network traffic captured during DDoS attack simulations in a Software Defined IoT (SD-IoT) environment.

Traffic was generated using Mininet, Open vSwitch, and Ryu SDN Controller. DDoS attacks were simulated using hping3, and the network traffic was captured using tcpdump/Wireshark.

## Traffic Types

- Normal Traffic
- TCP SYN Flood
- ICMP Flood


## Capture Format

- Packet Capture (`.pcap`)
- Feature Dataset (`sample_dataset.csv`)

## Feature Extraction

Packet-level traffic was processed to extract statistical features for machine learning, including:

- Packet Count (`pkt_count`)
- Byte Count (`byte_count`)
- Flow Duration (`duration`)
- Packet Rate (`pkt_rate`)
- TCP SYN Count (`syn_count`)
