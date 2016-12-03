#!/usr/bin/env python

import sys

from itertools import izip_longest

total = 0
tris = [[int(x) for x in line.split()] for line in sys.stdin]

args = [iter(tris)] * 3
for x in izip_longest(*args):
    for tri in zip(*x):
        tri = sorted(tri)
        if tri[0] + tri[1] > tri[2]:
            total += 1

print total
