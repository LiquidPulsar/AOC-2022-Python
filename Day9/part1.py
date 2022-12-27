from pathlib import Path
import numpy as np

moves: dict[str,complex] = {
    'U' : 1j,
    'D' : -1j,
    'L' : -1,
    'R' : 1
}

h=hprev=t=0
seen={0}
with open(Path(__file__).parent / "input.txt") as file:
    for d,n in map(str.split,file):
        n = int(n)

        for _ in range(n):
            hprev = h
            h += moves[d]
            if abs((h-t).imag) > 1 or abs((h-t).real) > 1:
                t = hprev
            seen.add(t)
print(seen,len(seen))