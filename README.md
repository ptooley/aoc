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

Session token is the token in your session cookie from adventofcode.com. Can be given either as a
string or as a path to a file containing the string.  The token is most easily collected using the
developer tools in chromium or firefox.  N.B Keep it secret, keep it safe.
