#!/usr/bin/env python

import paramiko
import time

rtrsnmpuser = 'pysnmp'
rtrsnmpauth = 'galileo1'
rtrsnmpkey  = 'galileo1'

rtrs = {
  "pynet-sw2": {
    "ssh_port": 22, 
    "username": "admin1", 
    "eapi_port": 443, 
    "password": "99saturday", 
    "ip_addr": "184.105.247.73"
  }, 
  "pynet-sw3": {
    "ssh_port": 22, 
    "username": "admin1", 
    "eapi_port": 443, 
    "password": "99saturday", 
    "ip_addr": "184.105.247.74"
  }, 
  "pynet-rtr2": {
    "ssh_port": 22, 
    "username": "pyclass", 
    "password": "88newclass", 
    "snmp_port": 161, 
    "ip_addr": "184.105.247.71"
  }, 
  "pynet-jnpr-srx1": {
    "ssh_port": 22, 
    "username": "pyclass", 
    "password": "88newclass", 
    "ip_addr": "184.105.247.76", 
    "netconf_port": "830"
  }, 
  "pynet-sw1": {
    "ssh_port": 22, 
    "username": "admin1", 
    "eapi_port": 443, 
    "password": "99saturday", 
    "ip_addr": "184.105.247.72"
  }, 
  "pynet-sw4": {
    "ssh_port": 22, 
    "username": "admin1", 
    "eapi_port": 443, 
    "password": "99saturday", 
    "ip_addr": "184.105.247.75"
  }, 
  "pynet-rtr1": {
    "ssh_port": 22, 
    "username": "pyclass", 
    "password": "88newclass", 
    "snmp_port": 161, 
    "ip_addr": "184.105.247.70"
  }
}

#-----------

def main():
    rc = paramiko.SSHClient()
    rc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    rc.load_system_host_keys()

    rtr = rtrs['pynet-rtr2']
    rc.connect(rtr['ip_addr'], port=22, username=rtr['username'], password=rtr['password'], look_for_keys=False, allow_agent=False)

    shell = rc.invoke_shell()

    shell.send("term len 0\n")
    shell.send("show version\n")

    time.sleep(2)
    print shell.recv(5000)
    return
 
if __name__ == "__main__":
    main()
