#! /usr/bin/python

__author__ = "Marshall"

def read_pi_id(file_location):
    f = open(file_location, 'r')
    id = f.read()
    return id.strip()