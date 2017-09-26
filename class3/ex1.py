#!/usr/bin/env python

import snmp_helper
from datetime import datetime
import time
import json
import os.path
import email_helper

rtr = ('184.105.247.71', 161)
snmp_creds = ('pysnmp', 'galileo1', 'galileo1')
oids = {'RunningLastChanged':'1.3.6.1.4.1.9.9.43.1.1.1.0'}
save_file = 'last_change.json'
alert_address = 'jerry.bonner@gmail.com'

def get_config_change(router_port, snmp_creds):
    snmp_data  = snmp_helper.snmp_get_oid_v3(router_port, snmp_creds, oids['RunningLastChanged'])
    return snmp_helper.snmp_extract(snmp_data)

def get_last_config_change(filename):
    # check if file exists
    if (os.path.isfile(filename)):
        f = open(filename, 'r')
        data = json.load(f)
        return data['last_change']
    else:
        return 0 

def dump_last_config_change(last_change, filename):
    data = {'last_change' : last_change}

    with open(filename, 'w') as f:
        json.dump(data, f)

def send_email_alert(email, last_change, current_change):
    
    subject = "Config Change Alert!"
    message = "Last change %s / New Change %s" % (last_change, current_change)

    email_helper.send_mail(email, subject, message, 'test@twb-tech.com') 
   
def main():
    last_change = get_last_config_change(save_file)
    current_change = get_config_change(rtr, snmp_creds)

    # check if we've ever stored the last_change before, must be > 0
    if (last_change > 0):

        # has the config changed?
        if (last_change != current_change):
            dump_last_config_change(current_change, save_file) 
            send_email_alert(alert_address, last_change, current_change)
    else:
        # store config change for the first time
        dump_last_config_change(current_change, save_file)
 
if __name__ == "__main__":
    main()
