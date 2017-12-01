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
    
