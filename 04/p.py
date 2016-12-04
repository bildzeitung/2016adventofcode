#!/usr/bin/env python

import re
import sys
from collections import Counter

ROOMRE = re.compile(r'(.+)\[(.+)\]')


def isreal(sector, room, checksum):
    strack = ''.join([z[0] for z in sorted(Counter(room).most_common(),
                                           key=lambda (x, y): (-y, x)
                                           )][0:5])
    if strack == checksum:
        return sector

    return 0


total = 0
for line in sys.stdin:
    room, checksum = ROOMRE.search(line.strip()).groups()
    sector = int(room.split('-')[-1])
    room = ''.join(room.split('-')[:-1])

    total += isreal(sector, room, checksum)

print total
