#! /usr/bin/python

__author__ = "Marshall"

import requests
import json

POS_RESPONSE = "True"

def post_json(url, json):
    
    response = request.post(url, json=json)
    
    if (response.text == POS_RESPONSE):
        return True
    else: 
        return False
