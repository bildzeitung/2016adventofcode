#!/usr/bin/env python

import re
import sys
from collections import defaultdict

ROOMRE = re.compile(r'(.+)\[(.+)\]')


def isreal(room, checksum):
    track = defaultdict(list)
    for idx, letter in enumerate(room):
        track[letter].append(idx)

    strack = sorted(track,
                    cmp=lambda x, y: cmp(len(track[y]), len(track[x])) or cmp(x, y)
                    )[0:5]
    return not sum(x[0] != x[1] for x in zip(strack, checksum))


total = 0
for line in sys.stdin:
    room, checksum = ROOMRE.search(line.strip()).groups()
    sector = int(room.split('-')[-1])
    room = ''.join(room.split('-')[:-1])

    if isreal(room, checksum):
        total += sector

print total
