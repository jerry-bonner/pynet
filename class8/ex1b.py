#!/usr/bin/env python

import django
from net_system.models import NetworkDevice, Credentials

creds = [{'username': 'admin1', 'password':'99saturday'},{'username':'pyclass', 'password':'88newclass'}]

rtrs = {
  "pynet-sw2": {
    "port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip": "184.105.247.73",
    "device_type": "arista_eos"
  }, 
  "pynet-sw3": {
    "port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip": "184.105.247.74",
    "device_type": "arista_eos"
  }, 
  "pynet-rtr2": {
    "port": "22", 
    "username": "pyclass", 
    "password": "88newclass", 
    "ip": "184.105.247.71",
    "device_type": "cisco_ios" 
  }, 
  "pynet-jnpr-srx1": {
    "port": "22", 
    "username": "pyclass", 
    "password": "88newclass", 
    "ip": "184.105.247.76", 
    "netconf_port": "830",
    "device_type": "juniper" 
  }, 
  "pynet-sw1": {
    "port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip": "184.105.247.72",
    "device_type": "arista_eos" 
  }, 
  "pynet-sw4": {
    "port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip": "184.105.247.75",
    "device_type": "arista_eos" 
  }, 
  "pynet-rtr1": {
    "port": "22", 
    "username": "pyclass", 
    "password": "88newclass", 
    "ip": "184.105.247.70",
    "device_type": "cisco" 
  }
}

def main():

    django.setup()

    # Delete everything

    Credentials.objects.all().delete()
    NetworkDevice.objects.all().delete()

    dbCreds = []

    # Loop through creds and add if needed, then append the cred obj dbCreds
    for cred in creds:
        dbCred = Credentials.objects.get_or_create(username=cred['username'], password=cred['password'])
        dbCreds.append(dbCred[0])

    # Loop through routers
    for rtr,data in rtrs.iteritems():

        # Set the cred obj depending on rtr username 
        for dbCred in dbCreds:
            if data['username'] == dbCred.username:
                curCred = dbCred

        # Add device
        dbDevice = NetworkDevice.objects.get_or_create(
            device_name=rtr,
            device_type=data['device_type'],
            ip_address=data['ip'],
            port=data['port'],
            credentials=curCred)

if __name__ == '__main__':
    main()
