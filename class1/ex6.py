#!/usr/bin/env python

import yaml
import json

# create list with a dictionary with two keys

data = [1,2,3, { 'spot':'dog', 'garfield':'cat' }, 5, 6]

# dump expanded yaml to file

with open('ex6_dump_yaml.yml', 'w') as f:
    f.write(yaml.dump(data, default_flow_style=False))

# dump json to file

with open('ex6_dump_json.json', 'w') as f:
    f.write(json.dumps(data))
