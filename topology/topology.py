#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink


def topology():

    net = Mininet(
        controller=None,
        switch=OVSSwitch,
        link=TCLink,
        autoSetMacs=True
    )

    print("*** Adding controllers")

    c0 = net.addController(
        'c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6633
    )

    c1 = net.addController(
        'c1',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6634
    )

    c2 = net.addController(
        'c2',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6635
    )

    print("*** Adding switches")

    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')
    s8 = net.addSwitch('s8')

    print("*** Adding hosts")

    h1 = net.addHost('h1', ip='10.1.1.2')
    h2 = net.addHost('h2', ip='10.1.1.3')
    h3 = net.addHost('h3', ip='10.1.1.4')
    h4 = net.addHost('h4')
    h5 = net.addHost('h5', ip='10.1.1.6')
    h6 = net.addHost('h6', ip='10.1.1.11')
    h7 = net.addHost('h7', ip='10.1.1.8')
    h8 = net.addHost('h8')
    h9 = net.addHost('h9')
    h10 = net.addHost('h10')

    print("*** Creating links")

    # Host links
    net.addLink(h1, s1)
    net.addLink(s1, h2)

    net.addLink(h3, s2)
    net.addLink(s2, h4)

    net.addLink(h5, s3)
    net.addLink(s3, h6)

    net.addLink(h7, s4)
    net.addLink(s4, h8)

    net.addLink(h9, s5)
    net.addLink(s5, h10)

    # Switch links
    net.addLink(s1, s6)
    net.addLink(s2, s6)

    net.addLink(s2, s7)
    net.addLink(s3, s7)

    net.addLink(s3, s8)
    net.addLink(s4, s8)

    net.addLink(s4, s5)

    print("*** Starting network")

    net.build()

    c0.start()
    c1.start()
    c2.start()

    s1.start([c0])
    s2.start([c0])
    s3.start([c2])
    s4.start([c2])
    s5.start([c2])
    s6.start([c1])
    s7.start([c1])
    s8.start([c1])

    print("*** Running CLI")

    CLI(net)

    net.stop()


if __name__ == '__main__':
    topology()