#!/usr/bin/env python

import sys

discs = []
positions = []
for line in sys.stdin:
    line = line.strip()
    position = int(line.split()[3])
    disc = int(line.split()[-1][:-1])
    positions.append(position)
    discs.append(disc)

positions.append(11)
discs.append(0)

time = 0
while True:
    new = []
    for idx, x in enumerate(discs):
        value = (x + time + 1 + idx) % positions[idx]
        new.append(value)

    if len(set(new)) == 1:
        break

    time += 1

print time
