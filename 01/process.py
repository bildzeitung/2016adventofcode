#!/usr/bin/env python

import sys


DIR = ['N', 'E', 'S', 'W']  # turning right
CDIR = 0
LOC = {'x': 0, 'y': 0}

FACTORS = {'N': {'x': 0, 'y': 1},
           'E': {'x': 1, 'y': 0},
           'S': {'x': 0, 'y': -1},
           'W': {'x': -1, 'y': 0}
           }

for line in sys.stdin:
    turns = [x.strip() for x in line.split(',')]
    for turn in turns:
        d, c = turn[0], int(turn[1:])
        if d == 'R':
            CDIR = (CDIR + 1) % 4
        else:
            CDIR = (CDIR + 4 - 1) % 4
        f = FACTORS[DIR[CDIR]]
        LOC['x'] += f['x'] * c
        LOC['y'] += f['y'] * c

print 'DIST: %d' % (abs(LOC['x'] + LOC['y']))
