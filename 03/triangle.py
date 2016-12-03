#!/usr/bin/env python

import sys

print len(filter(None, (vals[0] + vals[1] > vals[2]
                        for vals in [sorted([int(x) for x in line.split()])
                        for line in sys.stdin])))
