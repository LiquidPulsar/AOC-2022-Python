from pathlib import Path
import re
# from functools import partial
HOME = Path(__file__).parent

with open(HOME/"input.txt") as file:
    *crates, names = iter(file.readline,"\n")
    stacks = [[] for _ in range(len(names.split()))]

    for line in reversed(crates):
        for stack,v in zip(stacks,line[1::4]):
            if v!=' ':
                stack.append(v)
    print(stacks)
    for line in file:
        v,f,t = map(int,line.split()[1::2])
        for _ in range(v):
            stacks[t-1].append(stacks[f-1].pop())
print(''.join(map(list.pop,stacks)))