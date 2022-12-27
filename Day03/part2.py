from pathlib import Path

HOME = Path(__file__).parent

def value(c):
    # print(27+c-ord("A") if c <= ord("Z") else 1+c-ord("a"))
    return 27+c-ord("A") if c <= ord("Z") else 1+c-ord("a")

def score(lines):
    return value(next(iter(
        set(lines[0]) & set(lines[1]) & set(lines[2])
    )))

from more_itertools import chunked

DATA = (HOME/"input.txt").read_bytes()
print(sum(map(score, chunked(DATA.splitlines(),3))))