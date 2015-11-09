#! /usr/bin/python

__author__ = "Marshall"

# Local 
import communication

# External
import threading
import Queue
import datetime
import json

queue = Queue.Queue()
event_codes = {'0':'CLOSE', '1':'OPEN', '2':'KNOCK', '3':'MAIL'}

def spawn_handlers(sensor_mac):
    sensor_thread = threading.Thread(target = communication.run_sensor_thread, args=(queue,sensor_mac))
    phone_thread = threading.Thread(target = communication.run_phone_thread, args=(queue,))
    sensor_thread.setDaemon(True)
    phone_thread.setDaemon(True)
    sensor_thread.start()
    phone_thread.start()
    

def receive(raspberry_id):
    while queue.empty():
        pass
        
    string = queue.get()
    event = parse_string(string, raspberry_id)
    return event

def parse_string(string, raspberry_id):
    parsed_json = {}
    
    if (string[0] == "{"): # string is already json
        parsed_json = json.loads(string)
        parsed_json['event'] = 'ID_SCAN'
    else: # string isn't a json
        parsed_json['event'] = event_codes[string]
        
    parsed_json['time'] = str(datetime.datetime.now())  # add timestamp
    parsed_json['raspberry'] = raspberry_id             # add raspberry_id
    
    return parsed_json