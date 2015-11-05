#! /usr/bin/python

__author__ = "Marshall"

# local
import communication
import internal

# packages
import requests
import json

DEBUG = True
FILE_LOCATION = "/home/pi/Desktop/source.id" # "C:/source.id"
DEFAULT_URL = "http://193.62.81.88:5000"

server_url
raspberry_id

if __name__ == "__main__":
    
    # Set server url
    if (len(sys.argv) > 0):
        server_url = str(arv[0])
    else:
        server_url = DEFAULT_URL
        print("No server URL specified, reverting to default: " + DEFAULT_URL)
        
    # Set raspberry id
    raspberry_id = communication.pi.read_pi_id(FILE_LOCATION)
    if (DEBUG):
        print("Source ID set to " + raspberry_id)
        
    while 1:
        latest_event = internal.events.receive(raspberry_id)
        if (DEBUG):
            print("Received event")
            print("Posting JSON: " + latest_event + " to server")
        
        success = communication.server.post_json(server_url, latest_event)
        if (DEBUG and success):
            print("HTTP post succeeded")
        
            