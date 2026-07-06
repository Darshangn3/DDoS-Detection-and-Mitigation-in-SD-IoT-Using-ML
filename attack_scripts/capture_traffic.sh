#!/usr/bin/env bash
#
# =============================================================================
# Script  : capture_traffic(Attack using syn_flood.sh or icmp_flood.sh)
#
# Description:
#   Captures network traffic from the specified Mininet interface and saves
#   it as 'attack_capture.pcap'. The generated PCAP can be used for:
#
#   • Wireshark packet analysis
#   • Feature extraction
#   • ML dataset generation
#
# Usage:
#   sudo ./capture_traffic.sh <Interface> [Duration]
#
# Example:
#   sudo ./capture_traffic.sh s1-eth2
#   sudo ./capture_traffic.sh s1-eth2 30
#
# Requirements:
#   • tcpdump
#   • Root privileges
#
# NOTE:
#   Run only in a controlled Mininet/Lab environment.
# =============================================================================


###############################################################################
# User Inputs
###############################################################################

INTERFACE="$1"
DURATION="${2:-30}"

# Output file is fixed
OUTPUT_FILE="attack_capture.pcap"

###############################################################################
# Check tcpdump Installation
###############################################################################

if ! command -v tcpdump >/dev/null 2>&1; then
    echo "Error: tcpdump is not installed."
    exit 1
fi

###############################################################################
# Verify Interface
###############################################################################

if ! ip link show "$INTERFACE" >/dev/null 2>&1; then
    echo "Error: Interface '$INTERFACE' not found."
    exit 1
fi

###############################################################################
# Display Capture Information
###############################################################################

echo "====================================================="
echo "         Network Traffic Capture"
echo "====================================================="
echo "Interface : $INTERFACE"
echo "Duration  : ${DURATION} seconds"
echo "Output    : $OUTPUT_FILE"
echo "====================================================="

###############################################################################
# Start Packet Capture
###############################################################################

echo
echo "Starting packet capture..."

sudo timeout "$DURATION" tcpdump \
    -i "$INTERFACE" \
    -n \
    -w "$OUTPUT_FILE"

###############################################################################
# Capture Completed
###############################################################################

echo
echo "====================================================="
echo "Traffic Capture Completed Successfully!"
echo "====================================================="
echo "Saved File : $OUTPUT_FILE"
echo

