#!/usr/bin/env python

import sys

twiddle = int(sys.argv[1])


def iswall(x, y):
    eqn = x * x + 3 * x + 2 * x * y + y + y * y + twiddle
    return bin(eqn).count('1') % 2

# print maze, to validate iswall()
for i in range(7):
    line = ''
    for j in range(10):
        if iswall(j, i):
            line += 'X'
        else:
            line += '.'
    print line

# solve maze
queue = [((1, 1), 0)]
visited = set()


def solve():
    while queue:
        loc, steps = queue.pop(0)

        if loc[0] < 0 or loc[1] < 0:
            continue

        if loc in visited:
            continue

        visited.add(loc)

        if iswall(loc[0], loc[1]):
            continue

        if loc == (31, 39):
            return steps

        steps += 1
        queue.append(((loc[0], loc[1] + 1), steps))
        queue.append(((loc[0], loc[1] - 1), steps))
        queue.append(((loc[0] + 1, loc[1]), steps))
        queue.append(((loc[0] - 1, loc[1]), steps))

print solve()
