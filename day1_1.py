#!/usr/bin/env python3

import sys

instr = sys.argv[1]

res = sum([int(instr[i]) for i in range(len(instr)) if instr[i] == instr[i-1]])

print(res)
