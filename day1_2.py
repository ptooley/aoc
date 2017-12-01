#!/usr/bin/env python3

import sys

instr = sys.argv[1]
ls = len(instr)

res = sum([int(instr[i]) for i in range(ls) if instr[i] == instr[(i+ls//2)%ls]])

print(res)
