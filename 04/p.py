#!/usr/bin/env python

import re
import sys
from collections import defaultdict

ROOMRE = re.compile(r'(.+)\[(.+)\]')


def isreal(room, checksum):
    # print room, checksum
    track = defaultdict(list)
    for idx, letter in enumerate(room):
        track[letter].append(idx)

    def decider(x, y):
        lx = len(track[x])
        ly = len(track[y])
        # print x, lx, y, ly
        if lx == ly:
            return ord(x) - ord(y)

        return ly - lx

    strack = sorted(track, cmp=decider)[0:5]
    # print track
    # print strack
    # print zip(strack, checksum)
    return not sum(x[0] != x[1] for x in zip(strack, checksum))


total = 0
for line in sys.stdin:
    room, checksum = ROOMRE.search(line.strip()).groups()
    sector = room.split('-')[-1]
    room = ''.join(room.split('-')[:-1])

    if isreal(room, checksum):
        print "%s is real" % room
        total += int(sector)

print total
