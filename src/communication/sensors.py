#! /usr/bin/python

__author__ = "Marshall"

"""
MACADD = 'D2:70:C8:15:2B:97'

# pygatt.util.reset_bluetooth_controller()
dev = pygatt.pygatt.BluetoothLEDevice(MACADD, app_options='-t random')
dev.connect()
do = dev.char_read_uuid('0xA001')
dev.disconnect()"""