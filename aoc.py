from collections import OrderedDict
import requests
import inspect

def get_input(day, sc=None):
    """Get personalised aoc input for the given day

    Required Arguments:
        day - integer from 1 - 25
        sc - path to file containing session cookie value, or value as string

    """

    try:
        day = int(day)
    except:
        raise ValueError("day must be a number")

    if day < 1 or day > 25:
        raise ValueError("day must be in the range 0 < day < 26")

    if sc is not None:
        try:
            with open(sc) as fh:
                sc = fh.read().strip()
        except:
            sc = sc.strip()
    else:
        raise ValueError("session cookie must be provided")

    url = "https://adventofcode.com/2017/day/{}/input".format(day)

    r = requests.get(url, cookies={'session':sc})

    if r.status_code == 200:
        return r.text.strip()

    else:
        raise IOError("Server responded {}: {}\n"
                      "This probably means you have a bad/expired "
                      "session cookie".format(r.status_code, r.reason))

def score(func):
    lines = inspect.getsourcelines(func)[0]
    chars = "".join(lines[1:])
    return -len(chars)

class aoccollection(object):
    """Handles running and scoring a set of AOC puzzle solving functions"""

    def __init__(self, cookie):
        """Create object and set session cookie data"""
        self.puzzles = OrderedDict()
        self.cookie = cookie

    def add_puzzle(self, day, puzzle):
        """Add puzzles, assumed added in order"""
        try:
            day = int(day)
        except:
            raise ValueError("day must be a number")

        if day < 1 or day > 25:
            raise ValueError("day must be in the range 0 < day < 26")

        self.puzzles.setdefault(day, []).append(puzzle)

    def run(self):
        """Run all puzzles using personalised input, printing results"""

        for day, puzzles in self.puzzles.items():
            dayinp = get_input(day, self.cookie)
            print("Day {}:".format(day))
            for puzzlenum, puzzle in enumerate(puzzles):
                res = puzzle(dayinp)
                print("\tPuzzle {}, Result: {}"
                      "".format(day, puzzlenum, res))


def run_and_score(self):
        """Run all puzzles using personalised input, giving results and code
        golf score.
        """
        totsc = 0
        for day, puzzles in self.puzzles.items():
            dayinp = get_input(day, self.cookie)
            print("Day {}:".format(day))
            for puzzlenum, puzzle in enumerate(puzzles):
                res = puzzle(dayinp)
                psc = score(puzzle)
                totsc += psc
                print("\tPuzzle {}, Result: {}, Score: {}"
                      "".format(day, puzzlenum, res, psc))
            print("")

        print("\nTotal Score: {}".format(totsc))
