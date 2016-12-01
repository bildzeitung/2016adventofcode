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
    current_dir = 0
    loc = (0, 0)  # (x, y)
    memo = set()  # memoize visited locations

    for line in sys.stdin:
        for turn in [x.strip() for x in line.split(',')]:
            d, c = turn[0], int(turn[1:])
            current_dir = DIRF[d](current_dir)
            for _ in range(c):
                loc = (loc[0] + FACTORS[current_dir][0],
                       loc[1] + FACTORS[current_dir][1])
                if loc in memo:
                    print 'DIST: %d' % (abs(loc[0]) + abs(loc[1]))
                    sys.exit(0)
                memo.add(loc)

    print 'SAD TROMBONE'


if __name__ == "__main__":
    main()
