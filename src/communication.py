#! /usr/bin/python

import requests
import subprocess
import pygatt
import time

__author__ = "Marshall"

POS_RESPONSE = "True"
MESSAGE_HEADER = "Message: "
PHONE_SUBPROCESS = ['stdbuf', '-oL', 'explorenfc-cardemulation']

DOOR_UUID = "0000a001-0000-1000-8000-00805f9b34fb"
MAIL_UUID = "0000a011-0000-1000-8000-00805f9b34fb"
KNOCK_UUID = "0000a021-0000-1000-8000-00805f9b34fb"


# SERVER
def post_json(url, event):
    try:
        response = requests.post(url, json=event)
        if response.text == POS_RESPONSE:
            return True
        else: 
            return False
    
    except requests.exceptions.RequestException as e:
        print e
        return False


# PI
def read_config(file_location):
    settings = {}
    with open(file_location, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped[0] != ";":
                split = stripped.split('=')
                settings[split[0]] = split[1]

    return settings


# SENSORS
def run_sensor_thread(queue, sensor_mac):
    while True:
        try:
            pygatt.util.reset_bluetooth_controller()
            dev = pygatt.pygatt.BluetoothLEDevice(sensor_mac, app_options='-t random')
            dev.connect()
            break
        except pygatt.BluetoothLEError:
            print("Bluetooth device not found. Waiting...")
            time.sleep(5)

    def on_door_event(handle, value):
        queue.put(str(value[0]))

    def on_post_event(handle, value):
        queue.put("3")

    def on_knock_event(handle, value):
        queue.put("2")

    dev.subscribe(DOOR_UUID, on_door_event)
    dev.subscribe(MAIL_UUID, on_post_event)
    dev.subscribe(KNOCK_UUID, on_knock_event)
    dev.run()


# PHONE
def run_phone_thread(queue):
    p = subprocess.Popen(PHONE_SUBPROCESS, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while 1:
        line = p.stdout.readline().strip()
        print line
        if MESSAGE_HEADER in line:
            line = line.replace(MESSAGE_HEADER, "", 1).strip()
            queue.put(line)
