#!/bin/bash

echo "Cleaning previous Mininet topology..."
sudo mn -c

echo "Starting Ryu Controller..."
ryu-manager --ofp-tcp-listen-port 6634 ddos_ml_ryu.py &

sleep 5

echo "Starting Mininet topology..."
sudo python3 topology.py

echo "Topology started."