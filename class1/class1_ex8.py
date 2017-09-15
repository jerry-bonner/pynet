#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse('cisco_ipsec.txt')

crypto_maps = cfg.find_objects(r"^crypto map CRYPTO")

for crypto_map in crypto_maps:
    for child in crypto_map.all_children:
        print(child.text)
