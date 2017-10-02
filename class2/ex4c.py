#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

rtrs = ('184.105.247.70', '184.105.247.71')
SNMP_COMM = 'galileo'
SNMP_PORT = 161
SNMP_SYSNAME = '1.3.6.1.2.1.1.5.0'
SNMP_SYSDESC = '1.3.6.1.2.1.1.1.0'

oids = (SNMP_SYSNAME, SNMP_SYSDESC)

for rtr in rtrs:
    for oid in oids:
        data =  snmp_get_oid((rtr, SNMP_COMM, SNMP_PORT), oid=oid)
        print snmp_extract(data)
