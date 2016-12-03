#!/usr/bin/env python

import sys

total = 0
for vals in [sorted([int(x) for x in line.split()]) for line in sys.stdin]:
    if vals[0] + vals[1] > vals[2]:
        total += 1

print total
