from pathlib import Path

storage = [[0]*1000 for _ in range(1000)]

with open(Path(__file__).parent / 'input.txt') as file:
    for line in file:
        segs = [[*map(int,s.split(","))] for s in line.split(" -> ")]
        for (sx,sy),(ex,ey) in zip(segs,segs[1:]):
            print(sx,sy,ex,ey)
            if sx == ex:
                for y in range(min(sy,ey),max(sy,ey)+1):
                    storage[y][sx] = 1
            else:
                for x in range(min(sx,ex),max(sx,ex)+1):
                    storage[sy][x] = 1

n = 0
while True:
    n += 1
    y,x = 0,500

    while True:
        # print(y)
        if storage[y+1][x] == 0:
            y += 1
        elif storage[y+1][x-1] == 0:
            x -= 1
            y += 1
        elif storage[y+1][x+1] == 0:
            x += 1
            y += 1
        else:
            storage[y][x] = 2
            break
        
        if y == 999:
            print(n - 1)
            exit()