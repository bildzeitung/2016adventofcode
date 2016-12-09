#!/usr/bin/env python

import sys

for line in sys.stdin:
    collect = ''
    is_collecting = False
    output = ''

    line = line.strip()
    idx = 0
    while idx < len(line):
        x = line[idx]
        idx += 1

        if x == '(':
            collect = ''
            is_collecting = True
            continue

        if x == ')':
            is_collecting = False
            span, repeats = [int(y) for y in collect.split('x')]
            print 'COLLECTED |%s|%s %s, %s' % (collect, idx, span, repeats)
            output += line[idx:idx+span] * repeats
            idx += span
            continue

        if is_collecting:
            collect += x
            continue

        output += x

    print '[%s]->' % len(output), output
