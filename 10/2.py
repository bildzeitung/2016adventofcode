#!/usr/bin/env python

import sys

from collections import defaultdict

bots = defaultdict(list)
outs = defaultdict(list)
instr = [x.strip() for x in sys.stdin]
while instr:
    command = instr.pop(0)
    ops = command.split()
    if ops[0] == 'value':
        val, bot = int(ops[1]), ops[-1]
        bots[bot].append(val)
        bots[bot] = sorted(bots[bot])
        continue

    if ops[0] != 'bot':
        raise Exception('bad command')

    # resolution
    bot = ops[1]
    if len(bots[bot]) != 2:
        instr.append(command)
        continue

    # low
    target = ops[6]
    if ops[5] == 'bot':
        bots[target].append(bots[bot][0])
        bots[target] = sorted(bots[target])
    else:
        outs[target].append(bots[bot][0])

    # high
    target = ops[-1]
    if ops[-2] == 'bot':
        bots[target].append(bots[bot][1])
        bots[target] = sorted(bots[target])
    else:
        outs[target].append(bots[bot][0])

print outs['0'][0] * outs['1'][0] * outs['2'][0]
