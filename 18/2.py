#!/usr/bin/env python

import sys

from itertools import izip

LINES = int(sys.argv[1])
RULES = ('^^.', '.^^', '^..', '..^')


def process_line(seed):
    seed = '.' + seed + '.'  # pad out the border
    return ''.join(['^' if ''.join(x) in RULES else '.'
                    for x in izip(seed[0:], seed[1:], seed[2:])])


total = 0
for line in sys.stdin:
    current = line.strip()
    total = len(current.replace('^', ''))
    for _ in range(LINES-1):
        current = process_line(current)
        total += len(current.replace('^', ''))

print 'safe', total
