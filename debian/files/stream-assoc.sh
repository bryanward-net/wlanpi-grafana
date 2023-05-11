#!/bin/bash
while true; do iw dev wlan0 link | ./iwlink-raw.py | ./tografana.sh assoc; done
