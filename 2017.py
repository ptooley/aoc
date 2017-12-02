#!/usr/bin/env python3

from aoc import aoccollection

puzzles = aoccollection("aocsession.txt")

def day_1_1(x):
    return sum(int(x[i]) for i in range(len(x)) if x[i]==x[i-1])
puzzles.add_puzzle(1, day_1_1)

def day_1_2(x):
    lx = len(x)
    return sum(int(x[i]) for i in range(lx) if x[i]==x[i-lx//2])
puzzles.add_puzzle(1, day_1_2)

def day_2_1(x):
    return sum(map(lambda z:max(z)-min(z), map(lambda y:[int(z) for z in y.split()],x.split("\n"))))
puzzles.add_puzzle(2, day_2_1)

def day_2_2(x):
    return sum(map(lambda y:sum(sum(c//z for z in y if c%z==0)-1 for c in y),map(lambda y:[int(z) for z in y.split()],x.split("\n"))))
puzzles.add_puzzle(2, day_2_2)


puzzles.run_and_score()

