#!/usr/bin/env python

import sys

from collections import deque

HEIGHT = 6
WIDTH = 50
display = [['.' for x in range(WIDTH)] for y in range(HEIGHT)]


def show():
    print '\n'.join(''.join(y) for y in display)
    print


for line in sys.stdin:
    command = line.strip().split()
    if command[0] == 'rect':
        x, y = [int(z) for z in command[1].split('x')]
        for row in range(y):
            for col in range(x):
                display[row][col] = '#'
    elif command[0] == 'rotate':
        if command[1] == 'column':
            x, amount = [int(z) for z in (command[2].replace('x=', ''), command[-1])]
            # slice out column
            old = [y[x] for y in display]
            new = deque(old)
            new.rotate(amount)
            for idx, _ in enumerate(display):
                display[idx][x] = new.popleft()
        elif command[1] == 'row':
            y, amount = [int(z) for z in (command[2].replace('y=', ''), command[-1])]
            new = deque(display[y])
            new.rotate(amount)
            display[y] = list(new)
        else:
            raise Exception('Bad %s' % command[1])
    else:
        raise Exception('Bad command %s' % command[0])

    show()

print sum(len(''.join(y).replace('.', '')) for y in display)
