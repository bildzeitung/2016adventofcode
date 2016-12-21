#!/usr/bin/env python

import sys

scramble = sys.argv[1]


def _swap(item, *args):
    if args[0] == 'position':
        frm, to = int(args[1]), int(args[4])
        t = list(item)
        t[frm], t[to] = t[to], t[frm]
        item = ''.join(t)
    else:  # letter
        item = item.replace(args[1], '.').replace(args[-1], args[1]).replace('.', args[-1])

    return item


def _rotate(item, *args):
    if args[0] == 'left':
        l = list(item)
        for _ in range(int(args[1])):
            l.insert(0, l.pop(-1))
        item = ''.join(l)
    elif args[0] == 'right':
        l = list(item)
        for _ in range(int(args[1])):
            l.append(l.pop(0))
        item = ''.join(l)
    elif args[0] == 'based':
        target = args[-1]
        idx = item.find(target)
        l = list(item)
        mapping = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 0, 0: 1}
        for _ in range(mapping[idx]):
            l.append(l.pop(0))
        item = ''.join(l)

    return item


def _reverse(item, *args):
    start, finish = int(args[1]), int(args[-1])
    return item[0:start] + ''.join(reversed(item[start:finish+1])) + item[finish+1:]


def _move(item, *args):
    to = int(args[1])
    frm = int(args[-1])

    l = list(item)
    x = l[frm]
    del l[frm]

    item = ''.join(l)
    item = item[:to] + x + item[to:]

    return item


commands = {'swap': _swap,
            'rotate': _rotate,
            'reverse': _reverse,
            'move': _move,
            }

for line in sys.stdin:
    line = line.strip()
    ops = line.split()

    new_scramble = commands[ops[0]](scramble, *ops[1:])
    print ops[0], scramble, new_scramble
    scramble = new_scramble

print 'FINAL', scramble
