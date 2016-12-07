#!/usr/bin/env python

import re
import sys

hypernets = re.compile(r'\[.+?\]')
abba = re.compile(r'(.)((?<!\1).)(\2\1)')

count = 0
for line in sys.stdin:
    if any(abba.search(x[1:-1]) for x in hypernets.findall(line.strip())):
        continue

    if any(abba.search(x) for x in hypernets.sub(',', line.strip()).split(',')):
        count += 1

print count
