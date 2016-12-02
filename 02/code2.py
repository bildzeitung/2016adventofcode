#!/bin/env python

import sys

PAD = [['x', 'x', '1', 'x', 'x'],
       ['x', '2', '3', '4', 'x'],
       ['5', '6', '7', '8', '9'],
       ['x', 'A', 'B', 'C', 'x'],
       ['x', 'x', 'D', 'x', 'x'],
       ]

cur = (0, 2)  # start at '5'

INSTR = {"U": (0, -1), "D": (0, 1),
         "L": (-1, 0), "R": (1, 0),
         }

for line in sys.stdin:
    for d in line.strip():
        new_cur = (max(0, min(cur[0] + INSTR[d][0], 4)),
                   max(0, min(cur[1] + INSTR[d][1], 4)))
        if PAD[new_cur[1]][new_cur[0]] != 'x':
            cur = new_cur

    print PAD[cur[1]][cur[0]]
