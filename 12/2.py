#!/usr/bin/env python

import sys

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
pc = 0


def _cpy(pc, src, dst):
    if src in 'abcd':
        registers[dst] = registers[src]
    else:
        registers[dst] = int(src)
    return pc + 1


def _inc(pc, reg):
    registers[reg] += 1
    return pc + 1


def _dec(pc, reg):
    registers[reg] -= 1
    return pc + 1


def _jnz(pc, reg, dst):
    if reg in 'abcd':
        value = registers[reg]
    else:
        value = int(reg)

    if value != 0:
        return pc + int(dst)

    return pc + 1


instructions = {'cpy': _cpy, 'inc': _inc, 'dec': _dec, 'jnz': _jnz}

memory = [line.strip() for line in sys.stdin]


while pc < len(memory):
    op = memory[pc].split()
    pc = instructions[op[0]](pc, *op[1:])

print registers
