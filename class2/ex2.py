#!/usr/bin/env python

"""
telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
"""

import telnetlib

TELNET_PORT = 23
TELNET_TIMEOUT = 3

def login(ip, username, password):

    c = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)
    c.read_until("name:", TELNET_TIMEOUT)
    c.write(username + "\n")
    c.read_until("word:", TELNET_TIMEOUT)
    c.write(password + "\n")
    r = c.read_until("#")
    c.write("term len 0" + "\n")
    r = c.read_until("#")
    
    return c

def send_cmd(c, cmd):
    cmd = cmd.rstrip()
    c.write(cmd + "\n")
    return c.read_until("#")

def remote_cmd(ip, cmd, username, password):

    c = login(ip, username, password)
    output = send_cmd(c, cmd)
    c.close()

    return output

if __name__ == "__main__":
    print(remote_cmd('184.105.247.70', 'show ip int br', 'pyclass', '88newclass'))
