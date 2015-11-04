__author__ = "Marshall"

import nxppy
import pygatt
import time
import socket
import sys

def createsocket():
	host = "localhost"
	port = 12000

	soc = socket.socket()
	soc.connect((host, port))
	return soc

def runclient(soc)
	while 1:
		sendjsons(soc)

def sendjsons(soc):
	jsons = ["{\"code\": 1}", "{\"code\": 2}", "{\"code\": 0}", "{\"code\": 2}", "{\"code\": 3}"]
	for json in jsons:
		soc.sendall(json + "\n")
		time.sleep(5)
    
if __name__ == "__main__":
	soc = createsocket()
	runclient(soc)

"""
mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        print(uid)
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)

MACADD = 'D2:70:C8:15:2B:97'

# pygatt.util.reset_bluetooth_controller()
dev = pygatt.pygatt.BluetoothLEDevice(MACADD, app_options='-t random')
dev.connect()
do = dev.char_read_uuid('0xA001')
dev.disconnect()"""

