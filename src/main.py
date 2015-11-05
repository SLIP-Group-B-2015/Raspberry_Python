#! /usr/bin/python

__author__ = "Marshall"

# local
import communication
import internal

# external
import sys
import json

DEBUG = True
FILE_LOCATION = "/home/pi/Desktop/source.id" # "C:/source.id"
DEFAULT_URL = "http://193.62.81.88:5000"

server_url = ""
raspberry_id = ""

if __name__ == "__main__":
    
    
    # Set server url
    if (len(sys.argv) > 1):
        server_url = str(sys.argv[1])
        print("Server URL set to: " + server_url)
    else:
        server_url = DEFAULT_URL
        print("No server URL specified, reverting to default: " + DEFAULT_URL)
        
    # Set raspberry id
    raspberry_id = communication.read_id(FILE_LOCATION)
    print("Source ID set to " + raspberry_id)
        
    
    # Spawn threads
    internal.spawn_handlers()
    
    while 1:
        latest_event = internal.receive(raspberry_id)
        if (DEBUG):
            print("Received event")
            print("Posting JSON: " + json.dumps(latest_event) + " to server")
        
        success = communication.post_json(server_url, latest_event)
        if (DEBUG and success):
            print("HTTP post succeeded")
        
            