#!/usr/bin/env python

import django
from netmiko import ConnectHandler
from net_system.models import NetworkDevice, Credentials
from pprint import pprint
import time
from datetime import datetime
from multiprocessing import Process, current_process

def dump_devices():
    for obj in NetworkDevice.objects.all():
        pprint(obj.__dict__)

def dump_credentials():
    for obj in Credentials.objects.all():
        pprint(obj.__dict__)

def show_version(ip, device_type, username, password):

    c = ConnectHandler(device_type=device_type,
        ip=ip,
        username=username,
        password=password)

    print c.send_command('show version') 

def main():

    start_time = datetime.now()

    django.setup()

    procs = []

    for device in NetworkDevice.objects.all():
        my_proc = Process(target=show_version, args=(device.ip_address,
            device.device_type,
            device.credentials.username,
            device.credentials.password))
        procs.append(my_proc)
        my_proc.start()

    for proc in procs:
        proc.join()

    print "Runtime : {}".format(datetime.now() - start_time)

if __name__ == '__main__':
    main()
