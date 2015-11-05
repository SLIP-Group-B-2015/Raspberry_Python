#! /usr/bin/python

__author__ = "Marshall"

def runprocess(soc):    
    p = subprocess.Popen(['stdbuf', '-oL', 'explorenfc-cardemulation'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while 1:
        retcode = p.poll() # returns None while subprocess is running
        if(retcode is not None):
            break
      
        line = p.stdout.readline()
        if (line != "Card Emulation started."):
            line = line.replace("Message: ","",1)
            sendjson(soc,line)
