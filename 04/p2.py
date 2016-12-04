#!/usr/bin/env python

import re
import sys

ROOMRE = re.compile(r'(.+)\[')
A = ord('a')

for line in sys.stdin:
    room = ROOMRE.search(line.strip()).groups()[0]
    room, sector = room.split('-')[:-1], int(room.split('-')[-1])
    decoded = ' '.join(''.join(
                chr((((ord(y) - A) + sector) % 26) + A) for y in x
                ) for x in room)

    if 'northpole' in decoded:
        print sector, decoded
