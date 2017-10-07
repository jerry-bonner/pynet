#!/usr/bin/env python

import pyeapi
import argparse

def check_vlan_exists(c, vlan):
   
    output = c.enable('show vlan')

    for configured_vlan in output[0]['result']['vlans']:
        if vlan == int(configured_vlan):
            return True

    return False

def configure_vlan(c, vlan, name):
    
    if not check_vlan_exists(c, vlan):
        
        cmds = []
        cmds.append("vlan {}".format(vlan))
        cmds.append("name {}".format(name))
        cmds.append("write memory")

        c.config(cmds)
    return


def unconfigure_vlan(c, vlan):
    
    if check_vlan_exists(c, vlan):
        
        cmds = []
        cmds.append("no vlan {}".format(vlan))
        cmds.append("write memory")

        c.config(cmds)
    else:
        print "VLAN does not exist"

    return

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-v', action='store', dest='vlan', help='VLAN')
    parser.add_argument('-n', action='store', dest='name', help='VLAN Name')
    parser.add_argument('-r', action='store_true', dest='remove', help='Remove VLAN?', default=False)

    args = vars(parser.parse_args())

    conn = pyeapi.connect_to('pynet-sw4')

    if args['remove']:
        print "Removing VLAN {}".format(args['vlan'])
        unconfigure_vlan(conn, int(args['vlan']))
    else:
        configure_vlan(conn, int(args['vlan']), args['name'])

if __name__ == "__main__":
    main()
