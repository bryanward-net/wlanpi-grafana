#!/bin/bash

/opt/wlanpi-grafana/check-token.sh

while true; do ./pihealth.sh | /opt/wlanpi-grafana/tografana.sh pihealth; sleep 60; done
