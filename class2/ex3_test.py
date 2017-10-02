#!/usr/bin/env python

from ex3 import mytelnet

a = mytelnet('184.105.247.70', 'pyclass', '88newclass')
print(a.send_command('show ip int br'))
