#!/usr/bin/env python

import pexpect

rtrsnmpuser = 'pysnmp'
rtrsnmpauth = 'galileo1'
rtrsnmpkey = 'galileo1'

rtrs = {
    "pynet-sw2": {
    "ssh_port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip_addr": "184.105.247.73"
  }, 
  "pynet-sw3": {
    "ssh_port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip_addr": "184.105.247.74"
  }, 
  "pynet-rtr2": {
    "ssh_port": "22", 
    "username": "pyclass", 
    "password": "88newclass", 
    "snmp_port": "161", 
    "ip_addr": "184.105.247.71"
  }, 
  "pynet-jnpr-srx1": {
    "ssh_port": "22", 
    "username": "pyclass", 
    "password": "88newclass", 
    "ip_addr": "184.105.247.76", 
    "netconf_port": "830"
  }, 
  "pynet-sw1": {
    "ssh_port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip_addr": "184.105.247.72"
  }, 
  "pynet-sw4": {
    "ssh_port": "22", 
    "username": "admin1", 
    "eapi_port": "443", 
    "password": "99saturday", 
    "ip_addr": "184.105.247.75"
  }, 
  "pynet-rtr1": {
    "ssh_port": "22", 
    "username": "pyclass", 
    "password": "88newclass", 
    "snmp_port": "161", 
    "ip_addr": "184.105.247.70"
  }
}
#-----------


def main():

    rtr = rtrs['pynet-rtr2']

    c = pexpect.spawn("ssh -l {} {} -p {}".format(rtr['username'], rtr['ip_addr'], rtr['ssh_port']))
    c.timeout = 10 
    
    c.expect('assword:')
    c.sendline(rtr['password'])

    c.expect('#')

    c.sendline("conf t")

    c.expect('#')
    
    c.sendline("logging buffered 10001")

    c.expect('#')

    c.sendline("end")
    
    c.expect('#')
   
    c.sendline("show run | I logging buffered")

    c.expect('#')

    print c.before 
    
    return
 
if __name__ == "__main__":
    main()
