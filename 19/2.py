#!/usr/bin/env python

import sys

elves = int(sys.argv[1])

brute = range(1, elves + 1)
idx = 0
while len(brute) > 1:
    length = len(brute)
    toremove = (idx + length / 2) % length
    # print idx, 'removing', toremove, brute[toremove], brute
    del brute[toremove]
    if idx < toremove:
        idx += 1

    idx = idx % (length - 1)

print brute
