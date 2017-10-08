#!/usr/bin/env python

import django
from net_system.models import NetworkDevice, Credentials
from pprint import pprint

rtrs = {
  "test-sw1": {
    "port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip": "1.1.1.1",
    "device_type": "arista_eos"
  }, 
  "test-sw2": {
    "port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip": "2.2.2.2",
    "device_type": "arista_eos"
  } 
}

def dump_devices():
    for obj in NetworkDevice.objects.all():
        pprint(obj.__dict__)

def dump_credentials():
    for obj in Credentials.objects.all():
        pprint(obj.__dict__)

def main():

    django.setup()

    curCred = Credentials.objects.get(username='admin1')

    # Add Device
   
    dbDevice = NetworkDevice(
        device_name='test-sw4',
        device_type='cisco',
        ip_address='2.2.2.2',
        port='22',
        vendor='cisco',
        credentials=curCred)

    dbDevice.save()
    
    # Add device get_or_create
    dbDevice = NetworkDevice.objects.get_or_create(
        device_name='test-sw5',
        device_type='cisco',
        ip_address='2.2.2.2',
        port='22',
        vendor='cisco',
        credentials=curCred)

    dump_devices()
    dump_credentials()

if __name__ == '__main__':
    main()
