#!/bin/bash
/opt/wlanpi-grafana/check-token.sh

while true; do ./nlscan-lp wlan0 | /opt/wlanpi-grafana/tografana.sh scan; done
