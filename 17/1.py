#!/usr/bin/env python

import md5
import sys

DIRS = ['U', 'D', 'L', 'R']


def isok(direction, location):
    if direction == 'U' and location[1] - 1 > -1:
        return True

    if direction == 'D' and location[1] + 1 < 4:
        return True

    if direction == 'L' and location[0] - 1 > -1:
        return True

    if direction == 'R' and location[0] + 1 < 4:
        return True

    return False


passcode = sys.argv[1]
original = passcode
loc = (0, 0)

moveq = [(loc, passcode)]

while moveq:
    cloc, cpass = moveq.pop(0)
    print 'Considering', cloc, cpass
    if cloc == (3, 3):
        print 'VICTORY'
        print 'Passcode:', cpass.replace(original, '')
        break

    doors = [DIRS[idx] if x in 'bcdef' else None
             for idx, x in enumerate(md5.new(cpass).hexdigest()[0:4])]
    doors = [x for x in doors if x and isok(x, cloc)]

    print 'Doors:', doors, md5.new(cpass).hexdigest()[0:4]

    for door in doors:
        newpasscode = cpass + door
        if door == 'U':
            newloc = (cloc[0], cloc[1]-1)
        if door == 'D':
            newloc = (cloc[0], cloc[1]+1)
        if door == 'L':
            newloc = (cloc[0]-1, cloc[1])
        if door == 'R':
            newloc = (cloc[0]+1, cloc[1])
        moveq.append((newloc, newpasscode))
