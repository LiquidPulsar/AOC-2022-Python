from pathlib import Path

storage = [[0]*1000 for _ in range(1000)]
max_y = float('-inf')

with open(Path(__file__).parent / 'input.txt') as file:
    for line in file:
        segs = [[*map(int,s.split(","))] for s in line.split(" -> ")]
        for (sx,sy),(ex,ey) in zip(segs,segs[1:]):
            max_y = max(max_y,sy,ey)
            print(sx,sy,ex,ey)
            if sx == ex:
                for y in range(min(sy,ey),max(sy,ey)+1):
                    storage[y][sx] = 1
            else:
                for x in range(min(sx,ex),max(sx,ex)+1):
                    storage[sy][x] = 1

storage[max_y + 2] = [1]*1000

def display(xs,ys):
    min_x, max_x = xs
    min_y, max_y = ys
    for y in range(min_y,max_y+1):
        for x in range(min_x,max_x+1):
            v = storage[y][x]
            if v == 0:
                print(end=".")
            elif v == 1:
                print(end="#")
            else:
                print(end="o")
        print()

n = 0
while storage[0][500] == 0:
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
print(n)
display((490,510),(0,11))