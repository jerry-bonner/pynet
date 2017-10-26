#!/usr/bin/env python

from netmiko import ConnectHandler
from my_devices import rtrs

def main():
    conn = ConnectHandler(**rtrs['pynet-rtr2'])
    output = conn.send_config_set("logging buffered 10002")

    print output

    return
 
if __name__ == "__main__":
    main()
