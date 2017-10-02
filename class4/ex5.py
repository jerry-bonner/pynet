#!/usr/bin/env python

from netmiko import ConnectHandler

rtrsnmpuser = 'pysnmp'
rtrsnmpauth = 'galileo1'
rtrsnmpkey  = 'galileo1'

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
    
    c = ConnectHandler(**rtrs['pynet-rtr2'])
    c.config_mode()
    prompt = c.find_prompt()

    if (prompt.count('(config)#')):
        print "config mode confirmed."
    
    return
 
if __name__ == "__main__":
    main()
