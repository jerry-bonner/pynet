#!/usr/bin/env python

"""
telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
"""

import telnetlib.Telnet

def remote_cmd(ip, cmd, username, password):

        c = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)


if __name__ == "__main__":
    print(remote_cmd(
