#!/usr/bin/env python

import sys


CDIR = 0  # facing north
LOC = {'x': 0, 'y': 0}

FACTORS = [{'x': 0, 'y': 1},   # turning right, N
           {'x': 1, 'y': 0},   # E
           {'x': 0, 'y': -1},  # S
           {'x': -1, 'y': 0}   # W
           ]
DIRF = {'R': lambda x: (x+1) % 4,
        'L': lambda x: (x+4-1) % 4
        }

for line in sys.stdin:
    turns = [x.strip() for x in line.split(',')]
    for turn in turns:
        d, c = turn[0], int(turn[1:])
        CDIR = DIRF[d](CDIR)
        LOC['x'] += FACTORS[CDIR]['x'] * c
        LOC['y'] += FACTORS[CDIR]['y'] * c

print 'DIST: %d' % (abs(LOC['x']) + abs(LOC['y']))
