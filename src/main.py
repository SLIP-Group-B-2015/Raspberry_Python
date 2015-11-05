#! /usr/bin/python

__author__ = "Marshall"

# local
import communication
import internal

# external
import sys
import json

DEFAULT_LOCATION = "/home/pi/Desktop/config.ini" # "C:/source.id"
file_location = ""

if __name__ == "__main__":
    
    # Read command line args
	if (len(sys.argv) > 1):
        file_location = str(sys.argv[1])
        print("Config file set to: " + server_url)
    else:
        file_location = DEFAULT_LOCATION
        print("No config file specified, reverting to default: " + DEFAULT_LOCATION)
	
    # Read config file
	settings = communication.read_config(FILE_LOCATION)
	
	# Set debug level
	debug_str = settings['DEBUG']
	if debug_str == "True":
		DEBUG = True
	else:
		DEBUG = False
	
	# Set raspberry id
	raspberry_id = settings['RASPBERRY_ID']
    print("Source ID set to " + raspberry_id)
	
	# Set sensor MAC address
	sensor_mac = settings['SENSOR_MAC']
    print("Sensor MAC address set to: " + sensor_mac)
	
	# Set server url
	server_url = settings['SERVER_URL']
    print("Server URL set to " + server_url)
    
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
        
            