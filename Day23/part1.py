from pathlib import Path

Point = tuple[int,int]
def boundingbox(elves:set[Point]):
    minx = min(x for x,_ in elves)
    maxx = max(x for x,_ in elves)
    miny = min(y for _,y in elves)
    maxy = max(y for _,y in elves)
    return minx,maxx,miny,maxy

def display(elves:set[Point]):
    minx,maxx,miny,maxy = boundingbox(elves)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) in elves:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()
    print()

elves = set()
with open(Path(__file__).parent / "input.txt") as file:
    for y, row in enumerate(file):
        for x, char in enumerate(row):
            if char == "#":
                elves.add((x, y))

nbs = [slice(3),slice(6,None),slice(None,None,3),slice(2,None,3)]
ts = [(0,-1),(0,1),(-1,0),(1,0)]
opts = [*zip(nbs,ts)]*2

for rnd in range(10):
    targets = {}
    duplicates = set()
    for x, y in elves:
        neighbours = [
            (x + dx, y + dy) in elves
            for dx, dy in (
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 0),
                (1e10,1e10), #here so there's 9 and we can slice
                (1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            )
        ]

        if not any(neighbours):
            target = x,y
        else:
            for vals,delta in opts[rnd%4:rnd%4+4]:
                # print(vals,delta)
                if not any(neighbours[vals]):
                    break
            else:
                delta = (0,0)
            target = (x+delta[0],y+delta[1])
        print((x,y),target)
        if target in targets:
            duplicates.add(target)
            old = targets[target]
            targets[old] = old
            targets[(x,y)] = (x,y)
        else:
            targets[target] = (x,y) # to, from
    
    # print(f'{elves=}')
    # print(f'{targets=}')
    # print(f'{duplicates=}')
    elves = set(targets) - duplicates
    # to_fix = {e for e in targets if e in duplicates}
    # print(elves)
    # print(to_fix)
    display(elves)
a,b,c,d = boundingbox(elves)
print((b-a+1)*(d-c+1)-len(list(elves)))