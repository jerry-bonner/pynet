#!/usr/bin/env python

import django
from net_system.models import NetworkDevice, Credentials
from pprint import pprint

def dump_devices():
    for obj in NetworkDevice.objects.all():
        pprint(obj.__dict__)

def dump_credentials():
    for obj in Credentials.objects.all():
        pprint(obj.__dict__)

def main():

    django.setup()

    # Del Device
  
    NetworkDevice.objects.filter(device_name='test-sw4').delete()
    NetworkDevice.objects.filter(device_name='test-sw5').delete()
    dump_devices()
    dump_credentials()

if __name__ == '__main__':
    main()
