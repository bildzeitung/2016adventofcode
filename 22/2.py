#!/usr/bin/python

import sys
from collections import defaultdict

from itertools import permutations


DRIVES = {}

# skip header
_ = sys.stdin.readline()
_ = sys.stdin.readline()

for line in sys.stdin:
    new_line = line.strip().replace('  ', ' ')
    while new_line != line:
        line = new_line
        new_line = line.replace('  ', ' ')

    name, capacity, used, avail = new_line.split(' ')[0:4]
    capacity = int(capacity.replace('T', ''))
    used = int(used.replace('T', ''))
    avail = int(avail.replace('T', ''))
    DRIVES[name] = {'cap': capacity, 'used': used, 'avail': avail}

valid_pairs = 0
for item in permutations(DRIVES, 2):
    (a, b) = item

    if DRIVES[a]['used'] == 0:
        continue

    if DRIVES[a]['used'] > DRIVES[b]['avail']:
        continue

    if DRIVES[a]['used'] + DRIVES[b]['used'] < DRIVES[b]['cap'] and DRIVES[b]['used'] != 0:
        print 'Could consolidate', a, b

    valid_pairs += 1

print 'VALID:', valid_pairs

nodes = defaultdict(dict)
for name, drive in DRIVES.iteritems():
    x, y = [int(x[1:]) for x in name.split('-')[1:3]]
    nodes[y][x] = drive

print max(nodes) + 1, 'rows x', max(nodes[0].keys()) + 1, 'columns'

for y in range(0, max(nodes) + 1):
    row = nodes[y]
    print ' '.join(['{0}/{1}'.format(row[xx]['used'], row[xx]['cap']) for xx in sorted(row)])
