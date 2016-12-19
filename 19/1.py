#!/usr/bin/env python

import sys

elves = int(sys.argv[1])

total = 0
idx = 1
while True:
    total += idx
    if total >= elves:
        break
    idx *= 2

prev_total = total - idx
print 'sequence', idx, prev_total

seq = 1
while prev_total < elves - 1:
    seq += 2
    prev_total += 1

print 'Elf', seq
