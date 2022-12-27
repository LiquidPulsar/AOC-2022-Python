from collections import defaultdict
from pathlib import Path
import re
from tqdm import tqdm, trange

def man_dist(x1:int,y1:int,x2:int,y2:int) -> int:
    return abs(x2-x1)+abs(y2-y1)

def diamond(x:int,y:int,dist:int,row:int) -> tuple[int,int]:
    d = dist - abs(row - y)
    return (max(0,x-d),min(top,x+d)) # inclusive range

def merge(points:list[tuple[int,int]]) -> list[tuple[int,int]]:
    points.sort()
    out = [points[0]]
    for s,e in points[1:]:
        if s <= out[-1][1]+1:
            out[-1] = (out[-1][0],max(e,out[-1][1]))
        else:
            out.append((s,e))
    return out

# s --- e
#   S --- E

points = defaultdict(list)
top = 4_000_001
# top = 20
with open(Path(__file__).parent / 'input.txt') as file:
    for line in tqdm(file):
        s_x,s_y, b_x,b_y = map(int,re.findall(r"-?\d+",line))
        d = man_dist(s_x,s_y,b_x,b_y)
        for y in range(max(0,s_y-d),min(top,s_y+d)+1):
            points[y].append(diamond(s_x,s_y,d,y))

# print(*diamond(0,0,2))

for y in trange(top+1):
    points[y] = merge(points[y])
    if len(points[y]) > 1:
        tqdm.write(f"{points[y]} {y}")
        tqdm.write(f"{(points[y][0][1]+1)*4_000_000+y}")
        break