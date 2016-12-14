#!/usr/bin/env python

import md5
import re
import sys

TRIPLE = re.compile(r'(.)\1\1')

salt = sys.argv[1]
precalcindex = 0
index = 0
found = 0
precalcs = []


def calcmore(idx):
    print 'Making more...', idx
    for x in range(10000):
        key = md5.new(salt + str(idx)).hexdigest()
        # key stretch
        for y in range(2016):
            key = md5.new(key).hexdigest()
        precalcs.append(key)
        idx += 1

    print '...done'
    return idx


while found < 64:
    if len(precalcs) < index + 1:
        precalcindex = calcmore(precalcindex)

    key = precalcs[index]
    index += 1
    match = TRIPLE.search(key)
    if match:
        if len(precalcs) < (index + 1000):
            precalcindex = calcmore(precalcindex)
        match = match.group(1) * 5
        for x in range(1000):
            if match in precalcs[index+x]:
                found += 1
                print 'Found key', index
                break

print '64th key:', index - 1
