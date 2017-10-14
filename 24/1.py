#!/usr/bin/python

import sys

maze = []
for line in sys.stdin:
    maze.append(list(line.strip()))


locations = {}


def locate(item):
    for y, line in enumerate(maze):
        try:
            return (line.index(item), y)
        except ValueError:
            pass


for loc in range(0, 10):
    coord = locate(str(loc))
    if coord:
        locations[str(loc)] = coord


print locations
