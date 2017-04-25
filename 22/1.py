#!/usr/bin/python

import sys

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

    valid_pairs += 1

print 'VALID:', valid_pairs
