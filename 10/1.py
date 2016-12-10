#!/usr/bin/env python

import sys

from collections import defaultdict

VICTORY = [17, 61]

bots = defaultdict(list)
instr = [x.strip() for x in sys.stdin]
while instr:
    command = instr.pop(0)
    ops = command.split()
    if ops[0] == 'value':
        val, bot = int(ops[1]), ops[-1]
        bots[bot].append(val)
        bots[bot] = sorted(bots[bot])
        if bots[bot] == VICTORY:
            break
        continue

    if ops[0] != 'bot':
        raise Exception('bad command')

    # resolution
    bot = ops[1]
    if len(bots[bot]) != 2:
        instr.append(command)
        # print 'Deferring', command
        continue

    # low
    if ops[5] == 'bot':
        target = ops[6]
        bots[target].append(bots[bot][0])
        bots[target] = sorted(bots[target])
        if bots[bot] == VICTORY:
            break

    # high
    if ops[-2] == 'bot':
        target = ops[-1]
        bots[target].append(bots[bot][1])
        bots[target] = sorted(bots[target])
        if bots[bot] == VICTORY:
            break

    # print ops

for i, bot in bots.iteritems():
    if bot == VICTORY:
        print i, bot
