#!/bin/bash

sudo killall wpa_supplicant
sudo killall dhclient
sudo rm /var/lib/dhcp/dhclient.leases

sudo wpa_supplicant -iwlan0 -c/etc/wpa_supplicant/wpa_supplicant.conf -B
sudo dhclient wlan0
sudo /home/pi/Desktop/main.py
