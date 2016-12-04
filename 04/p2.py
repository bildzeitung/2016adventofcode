#!/usr/bin/env python

import re
import sys

ROOMRE = re.compile(r'(.+)\[(.+)\]')


for line in sys.stdin:
    room, _ = ROOMRE.search(line.strip()).groups()
    sector = int(room.split('-')[-1])
    decoded = ' '.join(''.join(
                [chr((((ord(y) - ord('a')) + sector) % 26) + ord('a')) for y in x]
                ) for x in room.split('-')[:-1])

    if 'northpole' in decoded:
        print sector, decoded
