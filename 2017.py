#!/usr/bin/env python3

from aoc import aoccollection

puzzles = aoccollection("aocsession.txt")

def day_1_1(x):
    return sum([int(x[i]) for i in range(len(x)) if x[i] == x[i-1]])
puzzles.add_puzzle(1, day_1_1)

def day_1_2(x):
    lx = len(x)
    return sum([int(x[i]) for i in range(lx) if x[i] == x[(i+lx//2)%lx]])
puzzles.add_puzzle(1, day_1_2)

puzzles.run_and_score()

