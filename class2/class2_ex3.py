import telnetlib
import time
import socket
import sys
import getpass

class mytelnet:

    TELNET_TIMEOUT = 6
    TELNET_PORT = 23

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.conn.write(cmd + '\n')
        time.sleep(1)
        return self.conn.read_very_eager()

    def login(self) :
        '''
        Login to network device
        '''
        output = self.conn.read_until("sername:", self.TELNET_TIMEOUT)
        self.conn.write(self.username + '\n')
        output += self.conn.read_until("ssword:", self.TELNET_TIMEOUT)
        self.conn.write(self.password + '\n')
        return output

    def disable_paging(self):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        paging_cmd='terminal length 0'
        return self.send_command(paging_cmd)

    def telnet_connect(self):
        '''
        Establish telnet connection
        '''
        try:
            return telnetlib.Telnet(self.ip, self.TELNET_PORT, self.TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

    def __init__(self, ip, username, password):
        print ip
        self.ip = ip
        self.username = username
        self.password = password

        self.conn = self.telnet_connect()
        self.login()
        self.disable_paging()
       
    def __del__(self):
        self.conn.close() 
