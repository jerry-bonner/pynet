#!/usr/bin/env python

import pyeapi

def main():

    conn = pyeapi.connect_to('pynet-sw4')
   
    cmds = ['show interfaces']

    output = conn.enable(cmds)

    # output[0]['result']['interfaces']['Management1']['interfaceCounters']['outOctets']

    for interface, data in output[0]['result']['interfaces'].iteritems():
        if 'interfaceCounters' in data.keys():
            print interface
            print "In : {}".format(data['interfaceCounters']['inOctets'])
            print "Out : {}".format(data['interfaceCounters']['outOctets'])
    return
 
if __name__ == "__main__":
    main()
