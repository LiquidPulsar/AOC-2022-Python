from pathlib import Path
from collections import defaultdict

space = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
faces = 0
with open(Path(__file__).parent / "input.txt") as f:
    for line in f:
        x,y,z = map(int, line.split(','))
        space[x][y][z] = True
        faces += 6 # assume none at x,y,z already
        for d in (-1,1):
            if space[x+d][y][z]: faces -= 2
            if space[x][y+d][z]: faces -= 2
            if space[x][y][z+d]: faces -= 2
print(faces)
