#!/usr/bin/env python

import django
from netmiko import ConnectHandler
from net_system.models import NetworkDevice, Credentials
from pprint import pprint
import time
from datetime import datetime

def dump_devices():
    for obj in NetworkDevice.objects.all():
        pprint(obj.__dict__)

def dump_credentials():
    for obj in Credentials.objects.all():
        pprint(obj.__dict__)

def main():

    start_time = datetime.now()
    django.setup()

    for device in NetworkDevice.objects.all():

        c = ConnectHandler(device_type=device.device_type,
            ip=device.ip_address,
            username=device.credentials.username,
            password=device.credentials.password)

        print c.send_command('show version')
    
    print "Runtime : {}".format(datetime.now() - start_time)

if __name__ == '__main__':
    main()
