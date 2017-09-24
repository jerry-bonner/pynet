#!/usr/bin/env python

import pygal
import time
import snmp_helper

rtr = ('184.105.247.71', 161)
snmp_creds = ('pysnmp', 'galileo1', 'galileo1')

alert_address = 'jerry.bonner@gmail.com'

descr_oid = '1.3.6.1.2.1.2.2.1.2.5'

oct_oids = {'ifInOctets_fa4':'1.3.6.1.2.1.2.2.1.10.5',
    'ifOutOctets_fa4':'1.3.6.1.2.1.2.2.1.16.5'}

oct_graph_file = "fa4_oct.svg"

pkt_oids = {'ifInUcastPkts_fa4':'1.3.6.1.2.1.2.2.1.11.5',
    'ifOutUcastPkts_fa4':'1.3.6.1.2.1.2.2.1.17.5'}

pkt_graph_file = "fa4_pkt.svg"

# Graph every x seconds
sample_time = 3

#-----------

def poll_snmp_oid(router_port, snmp_creds, oid):
    snmp_data = snmp_helper.snmp_get_oid_v3(router_port, snmp_creds, oid)
    return snmp_helper.snmp_extract(snmp_data)

def graph_snmp_data(xdata, sample_time, title, filename):

    # Create a Chart of type Line
    line_chart = pygal.Line()

    # Title
    line_chart.title = title

    # create x axis data based on num of samples * sample_time

    x_labels = []
   
    num_samples =  len(xdata.iteritems().next()[1])

    for i in range(0,num_samples):
       x_labels.append(sample_time * i)
 
    line_chart.x_labels = x_labels

    # Add each one of the above lists into the graph as a line with corresponding label

    for mib,data in xdata.iteritems():
        print mib
        print data

        # process data

        prev_num = 0
        processed_xdata = []
        for num in data:
            if prev_num > 0:
                processed_xdata.append(int(num) - int(prev_num))
                prev_num = num
            else:
                prev_num = num

        print processed_xdata
 
        #line_chart.add('InPackets', fa4_in_packets)
        line_chart.add(mib, processed_xdata)

    # Create an output image file from this
    line_chart.render_to_file(filename)
 
if __name__ == "__main__":

    ifDesc = poll_snmp_oid(rtr, snmp_creds, descr_oid)

    data = {}

    # poll 12 times 
    t = 12 

    # initialize dicts

    oct_data = {}
    pkt_data = {}

    for name,oid in oct_oids.iteritems():
        oct_data[name] = []  

    for name,oid in pkt_oids.iteritems():
        pkt_data[name] = []  

    # loop and collect data in lists

    while t>1:

        for name,oid in oct_oids.iteritems(): 
            snmp_data = poll_snmp_oid(rtr, snmp_creds, oid)
            oct_data[name].append(snmp_data)

        for name,oid in pkt_oids.iteritems(): 
            snmp_data = poll_snmp_oid(rtr, snmp_creds, oid)
            pkt_data[name].append(snmp_data)

        # graph raw snmp data to file

        graph_snmp_data(oct_data, sample_time, ifDesc + " Bytes",   oct_graph_file)
        graph_snmp_data(pkt_data, sample_time, ifDesc + " Packets", pkt_graph_file)

        t = t-1

        time.sleep(sample_time) 
