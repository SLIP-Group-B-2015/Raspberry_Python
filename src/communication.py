#! /usr/bin/python

__author__ = "Marshall"

import requests
import subprocess
import time

# SERVER
POS_RESPONSE = "True"

def post_json(url, event):
    try:
        response = requests.post(url, json=event)
        if (response.text == POS_RESPONSE):
            return True
        else: 
            return False
    
    except requests.exceptions.RequestException as e:
        return False

# PI
def read_id(file_location):
    f = open(file_location, 'r')
    id = f.read()
    return id.strip()

# SENSORS
def run_sensor_thread(queue):
    while 1:
        pass

"""
MACADD = 'D2:70:C8:15:2B:97'
# pygatt.util.reset_bluetooth_controller()
dev = pygatt.pygatt.BluetoothLEDevice(MACADD, app_options='-t random')
dev.connect()
do = dev.char_read_uuid('0xA001')
dev.disconnect()
"""

# PHONE
def run_phone_thread(queue):    
    
    p = subprocess.Popen(['stdbuf', '-oL', 'explorenfc-cardemulation'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    while 1:
        #line = p.stdout.readline()
        time.sleep(3)
        line = "{\"user\":\"b67d69b1-aa3e-4d07-82af-7c4cc6a5d26f\"}"
        if (line != "Card Emulation started."):
            line = line.replace("Message: ","",1)
            queue.put(line)