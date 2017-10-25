#!/usr/bin/env python

from netmiko import ConnectHandler
from my_devices import rtrs

def main():
    conn = ConnectHandler(**rtrs['pynet-rtr2'])
    conn.send_config_set("ip logging buffered 10000")
    return
 
if __name__ == "__main__":
    main()
