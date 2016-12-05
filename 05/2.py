#!/usr/bin/env python

import md5
import sys

doorid = sys.argv[1]

counter = 0
doorhash = md5.new(doorid + '0').hexdigest()
code = list('--------')

while '-' in code:
    while True:
        doorhash = md5.new(doorid + str(counter)).hexdigest()
        counter += 1
        if str(doorhash).startswith('00000'):
            break

    print doorhash[5], counter

    try:
        position = int(doorhash[5])
    except ValueError:
        continue

    if position > 7 or code[position] != '-':
        continue

    code[position] = doorhash[6]

    print ''.join(code)
