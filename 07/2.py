#!/usr/bin/env python

import re
import sys


hypernets = re.compile(r'\[.+?\]')
aba = re.compile(r'(.)((?<!\1).)(\1)')

count = 0
for line in sys.stdin:
    all_babs = set()
    for hypernet in hypernets.findall(line.strip()):
        start = 0
        item = aba.search(hypernet[1:-1], start)
        babs = set()
        while item:
            babs.add(item.group(0))
            start = item.start(0) + 1
            item = aba.search(hypernet[1:-1], start)

        all_babs |= babs

    if not all_babs:
        continue

    all_abas = set()
    extranets = hypernets.sub(',', line.strip()).split(',')
    for extranet in extranets:
        start = 0
        item = aba.search(extranet, start)
        abas = set()
        while item:
            abas.add(item.group(0))
            start = item.start(0) + 1
            item = aba.search(extranet, start)

        all_abas |= abas

    if not all_abas:
        continue

    all_abas = set('%s%s%s' % (x[1], x[0], x[1]) for x in all_abas)

    if all_abas & all_babs:
        print all_abas, all_babs
        count += 1

print count
