from pathlib import Path
import re

with open(Path(__file__).parent / "input.txt") as file:
    *board,_,cmds = map(str.rstrip,file)
    # print(board,cmds)
    l = max(map(len,board))
    board = [s.ljust(l) for s in board]
    # print(board)
startpos = (len(board[0])-len(board[0].lstrip()))+0j
print(startpos)

movedict:list[complex] = [
    -1j, # up
    1,   # right
    1j,  # down
    -1,  # left
]

def wrap(pos:complex,look:int) -> complex:
    if look == 0:
        if pos.imag == 0 or board[int(pos.imag)-1][int(pos.real)]==' ':
            for y in range(len(board)-1,-1,-1):
                if board[y][int(pos.real)] != ' ':
                    return complex(int(pos.real),y)
        elif board[int(pos.imag)-1][int(pos.real)]=='#':
            return pos
        else:
            return pos-1j
    elif look == 1:
        if pos.real == len(board[int(pos.imag)])-1 or board[int(pos.imag)][int(pos.real)+1]==' ':
            for x in range(len(board[int(pos.imag)])):
                if board[int(pos.imag)][x] != ' ':
                    return complex(x,int(pos.imag))
        elif board[int(pos.imag)][int(pos.real)+1]=='#':
            return pos
        else:
            return pos+1
    elif look == 2:
        if pos.imag == len(board)-1 or board[int(pos.imag)+1][int(pos.real)]==' ':
            for y in range(len(board)):
                if board[y][int(pos.real)] != ' ':
                    return complex(int(pos.real),y)
        elif board[int(pos.imag)+1][int(pos.real)]=='#':
            return pos
        else:
            return pos+1j
    elif look == 3:
        # print(pos.imag,int(pos.real)-1)
        # print(board[int(pos.imag)])
        if pos.real == 0 or board[int(pos.imag)][int(pos.real)-1]==' ':
            for x in range(len(board[int(pos.imag)])-1,-1,-1):
                if board[int(pos.imag)][x] != ' ':
                    return complex(x,int(pos.imag))
        elif board[int(pos.imag)][int(pos.real) - 1] == '#':
            return pos
        else:
            return pos-1

    raise ValueError("Shouldn't be here")

clone = [*map(list,board)]
pos = startpos
look = 1
for cmd in re.findall(r'\d+|[LR]',cmds):
    match cmd:
        case 'L': look = (look-1)%4
        case 'R': look = (look+1)%4
        case n:
            for _ in range(int(n)):
                nxt = wrap(pos,look)
                if nxt == pos:
                    break
                clone[int(pos.imag)][int(pos.real)] = '^>v<'[look]
                pos = nxt
    print(pos)

for row in clone:
    print(*row)
print((pos.imag+1)*1000 + (pos.real+1)*4 + (look-1)%4)
