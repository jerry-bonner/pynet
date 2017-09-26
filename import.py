#!/usr/bin/env python

# Quick script to import values from a key = value file and dump json

import re
import json

rtrs = {}
for line in open('/tmp/blah', 'r'):
    m = re.search(r'(pynet.*)\(.*', line)
    if m:
        rtr = m.group(1)
        rtrs[rtr] = {}
    
    m = re.search(r'\s+(.*) = (.*)', line)
    if m:
        rtrs[rtr][m.group(1)] = m.group(2)

print json.dumps(rtrs, indent=2)
