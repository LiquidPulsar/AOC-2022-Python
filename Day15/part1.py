from pathlib import Path
import re

def man_dist(x1:int,y1:int,x2:int,y2:int) -> int:
    return abs(x2-x1)+abs(y2-y1)

def diamond(x:int,y:int,dist:int,row:int) -> tuple[int,int]:
    d = dist - abs(row - y)
    return (x-d,x+d) # inclusive range

def merge(points:list[tuple[int,int]]) -> list[tuple[int,int]]:
    points.sort()
    out = [points[0]]
    for s,e in points[1:]:
        if s <= out[-1][1]:
            out[-1] = (out[-1][0],max(e,out[-1][1]))
        else:
            out.append((s,e))
    return out

# s --- e
#   S --- E


beacons:set[tuple[int,int]] = set()
points:list[tuple[int,int]] = []
# row = 10
row = 2_000_000
with open(Path(__file__).parent / 'input.txt') as file:
    for line in file:
        s_x,s_y, b_x,b_y = map(int,re.findall(r"-?\d+",line))
        d = man_dist(s_x,s_y,b_x,b_y)
        if row == b_y:
            beacons.add((b_x,b_y))
        if d >= abs(s_y - row):
            print(s_x,s_y, b_x,b_y,d)
            points.append(diamond(s_x,s_y,d,row))

# print(*diamond(0,0,2))
print(points)
points = merge(points)
print(beacons)
print(points)
print(sum(e-s+1 for s,e in points)-len(beacons))