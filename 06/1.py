#!/usr/bin/env python

import sys

from collections import Counter
from itertools import izip

words = [line.strip() for line in sys.stdin]

part1 = []
part2 = []
for item in izip(*words):
    c = Counter(item).most_common()
    part1.append(c[0][0])
    part2.append(c[-1][0])

print ''.join(part1), ''.join(part2)
