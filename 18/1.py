#!/usr/bin/env python

import sys

from itertools import izip

LINES = int(sys.argv[1])
RULES = ('^^.', '.^^', '^..', '..^')


def process_line(seed):
    newline = ''
    seed = '.' + seed + '.'
    # print 'processing', seed
    for x in izip(seed[0:], seed[1:], seed[2:]):
        x = ''.join(x)
        if x in RULES:
            newline += '^'
        else:
            newline += '.'

    return newline


rows = []
total = 0
for line in sys.stdin:
    seed = line.strip()
    rows.append(seed)
    total += sum(x == '.' for x in seed)
    for _ in range(LINES-1):
        rows.append(process_line(rows[-1]))
        total += sum(x == '.' for x in rows[-1])

print '\n'.join(rows)
print 'safe', total
