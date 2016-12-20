#!/usr/bin/env python

import sys

ranges = []
for line in sys.stdin:
    start, finish = [int(x) for x in line.strip().split('-')]
    ranges.append((start, finish))

consolidated = [sorted(ranges, key=lambda x: x[0])[0]]
print consolidated
for item in sorted(ranges, key=lambda x: x[0])[1:]:
    last = consolidated[-1]
    # connected range
    if last[1] + 1 == item[0]:
        consolidated[-1] = (last[0], item[1])
        continue

    # disparate range
    if last[1] < item[0]:
        consolidated.append(item)
        continue

    # extend range
    if last[1] < item[1]:
        consolidated[-1] = (last[0], item[1])
        continue

print consolidated
current = consolidated[0]
for item in consolidated[1:]:
    diff = item[0] - current[1]
    if diff:
        print 'valid', item[1], current[1], diff, range(current[1]+1, item[0], 1)
        break
