from pathlib import Path
from tqdm import tqdm

with open(Path(__file__).parent / "input.txt") as file:
    lst = [*map(int,file)]

ordered = lst[:]
for e in ordered: # 0 1 2
    i = lst.index(e)
    lst.pop(i)
    o = (i+e)%len(lst)
    lst.insert(o,e)
    # print(lst)
i = lst.index(0)
print(lst[(i+1000)%len(lst)]
     +lst[(i+2000)%len(lst)]
     +lst[(i+3000)%len(lst)])