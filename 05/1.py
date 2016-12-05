#!/usr/bin/env python

import md5
import sys

doorid = sys.argv[1]

counter = 0

doorhash = md5.new(doorid + '0').hexdigest()
code = []

for _ in range(8):
    while True:
        doorhash = md5.new(doorid + str(counter)).hexdigest()
        counter += 1
        if str(doorhash).startswith('00000'):
            break
    print doorhash[5], counter
    code.append(doorhash[5])

print ''.join(code)
