#! /usr/bin/python

import requests
import subprocess

__author__ = "Marshall"

POS_RESPONSE = "True"
MESSAGE_HEADER = "Message: "
PHONE_SUBPROCESS = ['stdbuf', '-oL', 'explorenfc-cardemulation']


# SERVER
def post_json(url, event):
    try:
        response = requests.post(url, json=event)
        if response.text == POS_RESPONSE:
            return True
        else: 
            return False
    
    except requests.exceptions.RequestException:
        return False


# PI
def read_config(file_location):
    settings = {}
    with open(file_location, 'r') as f:
        for line in f:
            split = line.strip().split()
            settings[split[0]] = split[1]

    return settings


# SENSORS
def run_sensor_thread(queue, sensor_mac):
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
    
    p = subprocess.Popen(PHONE_SUBPROCESS, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    while 1:
        line = p.stdout.readline().strip()
        print(line)
        if MESSAGE_HEADER in line:
            line = line.replace(MESSAGE_HEADER, "", 1).strip()
            queue.put(line)
