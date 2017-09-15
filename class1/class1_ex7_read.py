#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

# create list with a dictionary with two keys

data = [1,2,3, { 'spot':'dog', 'garfield':'cat' }, 5, 6]

# dump expanded yaml to file

with open('class1_ex6_dump_json.json', 'r') as f:
    mylist = json.load(f)

pp(mylist)

with open('class1_ex6_dump_yaml.yml', 'r') as f:
    mylist = yaml.load(f)

pp(mylist)
