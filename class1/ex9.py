#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cfg = CiscoConfParse('cisco_ipsec.txt')

crypto_maps = cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for crypto_map in crypto_maps:
    print(crypto_map.text)
    for child in crypto_map.all_children:
        print(child.text)
