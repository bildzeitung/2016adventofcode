#!/usr/bin/env python

import sys


def dragon(a):
    return a + '0' + a[::-1].replace('1', 'a').replace('0', '1').replace('a', '0')


def checksum(a):
    while not(len(a) % 2):
        a = ''.join('1' if x == y else '0' for x, y in zip(a[::2], a[1::2]))
        print len(a)

    return a


seed = sys.argv[1]
length = int(sys.argv[2])

while len(seed) < length:
    seed = dragon(seed)
    print len(seed)

seed = seed[0:length]
print '---'
print checksum(seed)
