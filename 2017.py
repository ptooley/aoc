#!/usr/bin/env python3

from aoc import get_input, score

instr = get_input(1, "aocsession.txt")

def day_1_1(x):
    return sum([int(x[i]) for i in range(len(x)) if x[i] == x[i-1]])

def day_1_2(x):
    lx = len(x)
    return sum([int(x[i]) for i in range(lx) if x[i] == x[(i+lx//2)%lx]])

score(day_1_2)

print("Day 1 Puzzle 1 Result: {} Score: {}".format(day_1_1(instr), score(day_1_1)))
print("Day 1 Puzzle 2 Result: {} Score: {}".format(day_1_2(instr), score(day_1_2)))

