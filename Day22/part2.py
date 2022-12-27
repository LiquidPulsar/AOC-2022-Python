from dataclasses import dataclass
from pathlib import Path
from itertools import product
import re

with open(Path(__file__).parent / "input.txt") as file:
    *board,_,cmds = map(str.rstrip,file)
    # print(board,cmds)
    l = max(map(len,board))
    board = [s.ljust(l) for s in board]
    # print(board)

@dataclass
class Coord:
    x: int
    y: int

    def __add__(self,other):
        return Coord(self.x+other.x,self.y+other.y)

movedict:list[Coord] = [
    Coord(0,-1), # up
    Coord(1,0),  # right
    Coord(0,1),  # down
    Coord(-1,0)  # left
]

class Face:
    CS = 50
    up: 'Face'
    right: 'Face'
    down: 'Face'
    left: 'Face'
    def __init__(self,offset:Coord):
        self.offset = offset

        print(len(board),offset.y)
        print(len(board[offset.y]),offset.x)
        self.board = [board[y][offset.x:offset.x+50] 
            for y in range(offset.y,offset.y+self.CS)]

        self.display = [*map(list,self.board)]

    @property
    def dirs(self):
        return self.up,self.right,self.down,self.left

    def along(self,coord,facing):
        return (coord[0],
                coord[1],
                coord[0],
                coord[1])[facing]

    def enter(self,from_,dir_,val):
        if self.up is from_:
            if dir_ in (0,1):
                return Coord(Face.CS-val-1, 0),2
            return Coord(val, 0),2 #coord, facing
        elif self.right is from_:
            if dir_ in (0,1):
                return Coord(Face.CS-1, Face.CS-val-1),3
            return Coord(Face.CS-1,val),3
        elif self.down is from_:
            if dir_ in (2,3):
                return Coord(Face.CS-val-1, Face.CS-1),0
            return Coord(val, Face.CS-1),0
        elif self.left is from_:
            if dir_ in (2,3):
                return Coord(0, Face.CS-val-1),1
            return Coord(0, val),1
        print("Shouldn't be here")
    
    def move(self,coord:Coord,facing:int) -> tuple['Face',Coord,int]:
        print(coord,facing)
        self.display[coord.y][coord.x] = '^>v<'[facing]
        nxt = coord + movedict[facing]
        if nxt.x < 0:
            nxt,nfacing = self.left.enter(self,3,coord.y)
            if self.left[nxt] != '#':
                return self.left,nxt,nfacing
        elif nxt.x >= Face.CS:
            nxt,nfacing = self.right.enter(self,1,coord.y)
            if self.right[nxt] != '#':
                return self.right,nxt,nfacing
        elif nxt.y < 0:
            nxt,nfacing = self.up.enter(self,0,coord.x)
            if self.up[nxt] != '#':
                return self.up,nxt,nfacing
        elif nxt.y >= Face.CS:
            nxt,nfacing = self.down.enter(self,2,coord.x)
            if self.down[nxt] != '#':
                return self.down,nxt,nfacing
        elif self[nxt] != '#':
            return self,nxt,facing
        return self,coord,facing


    def __getitem__(self,coord:tuple[int,int]|Coord): # self[x,y] or self[(x,y)]
        if isinstance(coord,Coord):
            coord = coord.x,coord.y
        return self.board[coord[1]][coord[0]]

def setup_test():
    A = Face(Coord(8,0))
    B = Face(Coord(0,4))
    C = Face(Coord(4,4))
    D = Face(Coord(8,4))
    E = Face(Coord(8,8))
    F = Face(Coord(12,8))
    
    A.right = F
    B.right = C
    C.right = D
    D.right = F
    E.right = F
    F.right = A

    A.down = D
    B.down = E
    C.down = E
    D.down = E
    E.down = B
    F.down = B

    A.left = C
    B.left = F
    C.left = B
    D.left = C
    E.left = C
    F.left = E

    A.up = B
    B.up = A
    C.up = A
    D.up = A
    E.up = D
    F.up = D

    return A,B,C,D,E,F
# A,B,C,D,E,F = setup_test()

def setup():
    A = Face(Coord(50,0))
    B = Face(Coord(100,0))
    C = Face(Coord(50,50))
    D = Face(Coord(50,100))
    E = Face(Coord(0,100))
    F = Face(Coord(0,150))

    A.right = B
    B.right = D
    C.right = B
    D.right = B
    E.right = D
    F.right = D

    A.down = C
    B.down = C
    C.down = D
    D.down = F
    E.down = F
    F.down = B

    A.left = E
    B.left = A
    C.left = E
    D.left = E
    E.left = A
    F.left = A

    A.up = F
    B.up = F
    C.up = A
    D.up = C
    E.up = C
    F.up = E

    return A,B,C,D,E,F
A,B,C,D,E,F = setup()

curr,coord,facing = A,Coord(0,0),1
for cmd in re.findall(r'\d+|[LR]',cmds):
    if cmd == 'L':
        facing = (facing-1)%4
    elif cmd == 'R':
        facing = (facing+1)%4
    else:
        for _ in range(int(cmd)):
            curr,coord,facing = curr.move(coord,facing)
        print(curr,coord,facing)

t = curr.offset + coord + Coord(1,1)
print(t.y*1000 + t.x*4 + (facing-1)%4)

final = [[' ']*Face.CS*4 for _ in range(Face.CS*4)]
for face in A,B,C,D,E,F:
    for y, x in product(range(Face.CS), repeat=2):
        final[face.offset.y+y][face.offset.x+x] = face.display[y][x]

for line in final:
    print(''.join(line))