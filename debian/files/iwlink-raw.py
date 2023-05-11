#!/usr/bin/env python3
import sys
import json

data = list(sys.stdin)


#Connected to d4:20:b0:93:7e:f2 (on wlan0)
#      SSID: AP12Test
#      freq: 5180
#      RX: 73173077 bytes (441010 packets)
#      TX: 1394 bytes (19 packets)
#      signal: -45 dBm
#      rx bitrate: 573.5 MBit/s 40MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
#      tx bitrate: 573.5 MBit/s 40MHz HE-MCS 11 HE-NSS 2 HE-GI 0 HE-DCM 0
#
#      bss flags:        short-slot-time
#      dtim period:      2
#      beacon int:       100


assert "Connected to" in data[0]
bssid = data[0][13:30]
ssid = data[1].strip().split(":")[1].strip().replace(" ", "\ ")
freq = data[2].strip().split(":")[1].strip()
rx_b = data[3].strip().split(":")[1].strip().split(" ")[0]
tx_b = data[4].strip().split(":")[1].strip().split(" ")[0]
rx_p = data[3].strip().split(":")[1].strip().split(" ")[2][1:]
tx_p = data[4].strip().split(":")[1].strip().split(" ")[2][1:]
signal = data[5].strip().split(":")[1].strip().split(" ")[0]
rx_br = data[6].strip().split(":")[1].strip().split(" ")[0]
tx_br = data[7].strip().split(":")[1].strip().split(" ")[0]

print(f'wlanpi,associated=true,assoc_ssid={ssid},assoc_bssid={bssid} rssi={signal},freq={freq},rx_bytes={rx_b},rx_packets={rx_p},tx_bytes={tx_b},tx_packets={tx_p},rx_bitrate={rx_br},tx_bitrate={tx_br}')


