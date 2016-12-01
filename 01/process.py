#!/usr/bin/env python

import sys


FACTORS = ((0, 1),   # turning right, N
           (1, 0),   # E
           (0, -1),  # S
           (-1, 0)   # W
           )
DIRF = {'R': lambda x: (x+1) % 4,
        'L': lambda x: (x-1) % 4
        }


def main():
    current_dir = 0  # facing north
    loc = (0, 0)
    for line in sys.stdin:
        for turn in [x.strip() for x in line.split(',')]:
            d, c = turn[0], int(turn[1:])
            current_dir = DIRF[d](current_dir)
            loc = (loc[0] + FACTORS[current_dir][0] * c,
                   loc[1] + FACTORS[current_dir][1] * c)

    print 'DIST: %d' % (abs(loc[0]) + abs(loc[1]))


if __name__ == "__main__":
    main()
