# AoCgolf

My solutions for the advent of code 2017.  

Includes a set of utility functions (aoc.py) to allow fetching personalised Advent of Code input
data, running collections of code snippets and scoring based on brevity of code.

Example:
```
from aoc import aoccollection

puzzles = aoccollection("sessiontoken")

def mysolution(x):
  return len(x)

puzzles.add_puzzle(day=1, puzzle=mysolution)

puzzles.run_and_score()
```
