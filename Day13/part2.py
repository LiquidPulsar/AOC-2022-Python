from pathlib import Path
from ast import literal_eval
from functools import cmp_to_key

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

def smaller_(a,b): # functool needs a <0 value to signal __lt__
    return -smaller(a,b)

with open(Path(__file__).parent / "input.txt") as file:
    packets = [literal_eval(line) for line in file if line.strip()]
packets.extend(([[2]], [[6]]))
packets.sort(key=cmp_to_key(smaller_))
print(*packets,sep='\n')
print((packets.index([[2]])+1)*(packets.index([[6]])+1))