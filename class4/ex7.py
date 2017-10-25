#!/usr/bin/env python

from netmiko import ConnectHandler
from my_devices import rtrs

def main():
    conn = ConnectHandler(**rtrs['pynet-rtr2'])
    conn.config_mode()
    conn.send_command("ip logging buffered 10000")
    conn.enable()
    conn.send_command("write memory")
    return
 
if __name__ == "__main__":
    main()
