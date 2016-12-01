#!/usr/bin/env python

import sys


CDIR = 0
LOC = {'x': 0, 'y': 0}
ALL = []

FACTORS = [{'x': 0, 'y': 1},
           {'x': 1, 'y': 0},
           {'x': 0, 'y': -1},
           {'x': -1, 'y': 0}
           ]
DIRF = {'R': lambda x: (x+1) % 4,
        'L': lambda x: (x+4-1) % 4
        }

for line in sys.stdin:
    for turn in [x.strip() for x in line.split(',')]:
        d, c = turn[0], int(turn[1:])
        CDIR = DIRF[d](CDIR)
        for _ in range(c):
            LOC['x'] += FACTORS[CDIR]['x']
            LOC['y'] += FACTORS[CDIR]['y']
            encode = '%d|%d' % (LOC['x'], LOC['y'])
            if encode in ALL:
                print 'DIST: %d' % (abs(LOC['x']) + abs(LOC['y']))
                sys.exit(0)
            ALL.append(encode)

print 'SAD TROMBONE'
