#!/usr/bin/env python

import sys


def resolve(line):
    collect = ''
    is_collecting = False
    output = 0
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
            output += resolve(line[idx:idx+span]) * repeats
            idx += span
            continue

        if is_collecting:
            collect += x
            continue

        output += 1

    return output


for line in sys.stdin:
    line = line.strip()
    print '[%s]' % resolve(line)
