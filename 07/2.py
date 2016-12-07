#!/usr/bin/env python

import re
import sys


hypernets = re.compile(r'\[.+?\]')
aba = re.compile(r'(.)((?<!\1).)(\1)')


def findall_overlapping(item):
    rvs = set()
    start = 0
    match = aba.search(item, start)
    while match:
        rvs.add(match.group(0))
        start = match.start(0) + 1
        match = aba.search(item, start)
    return rvs


count = 0
for line in sys.stdin:
    all_babs = reduce(lambda x, y: x | findall_overlapping(y),
                      hypernets.findall(line.strip()),
                      set())

    all_abas = set('%s%s%s' % (x[1], x[0], x[1])
                   for x in reduce(lambda x, y: x | findall_overlapping(y),
                                   hypernets.sub(',', line.strip()).split(','),
                                   set()))

    if all_abas & all_babs:
        print all_abas, all_babs
        count += 1

print count
