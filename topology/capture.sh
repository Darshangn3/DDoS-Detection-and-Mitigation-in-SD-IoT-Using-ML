#!/bin/bash

echo "Capturing packets..."
sudo tcpdump -i any -w sample_capture.pcap