from pathlib import Path
from ast import literal_eval

def smaller(a,b): #0 larger, 1 eq, 2 smaller so <= have true val
    for c1,c2 in zip(a,b):
        if isinstance(c1,list):
            if isinstance(c2,int):
                c2 = [c2]
            v = smaller(c1,c2)
            if v in (0,2): return v
        elif isinstance(c2,list):
            v = smaller([c1],c2)
            if v in (0,2): return v
        elif c1 < c2:
            return 2
        elif c1 > c2:
            return 0
    if len(a) < len(b):
        return 2
    elif len(a) > len(b):
        return 0
    return 1

with open(Path(__file__).parent / "input.txt") as file:
    t = 0
    for i,(a,b) in enumerate(map(str.splitlines,file.read().split('\n\n')),1):
        a,b = map(literal_eval,(a,b))
        if smaller(a,b): #right order if eq
            t += i
    print(t)