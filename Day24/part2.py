from collections import deque
from pathlib import Path
import numpy as np

def update_board(boards):
    #np.roll(x,dist,0 vert 1 hor)
    _,up,right,down,left = boards
    up = np.roll(up,-1,0)
    right = np.roll(right,1,1)
    down = np.roll(down,1,0)
    left = np.roll(left,-1,1)
    total = up | right | down | left
    # printout(total)
    return total,up,right,down,left

def neighbours(pos):
    if pos in [(0, -1), true_end]:
        yield pos
    x,y = pos
    for dx,dy in ((0,1),(0,-1),(1,0),(-1,0),(0,0)):
        new_y = y+dy
        new_x = x+dx
        # print(new_x,new_y,...)
        if (
            new_y >= 0
            and new_x >= 0
            and new_y < len(board[0])
            and new_x < len(board[0][0])
            and not board[0][y + dy, x + dx]
        ):
            yield new_x,new_y

def printout(arr):
    lst = np.where(arr,'X','.').tolist()
    for row in lst:
        print(''.join(row))
    print()
    print()

board = (Path(__file__).parent / "input.txt").read_text().splitlines()
board = [*map(list,board)]
board = np.array(board)[1:-1,1:-1] #only inside
up = board=='^'
right = board=='>'
down = board=='v'
left = board=='<'
total = up | right | down | left
board = total,up,right,down,left
board = update_board(board) #play into next turn's board
printout(board[0])
# for b in board:
#     printout(b)

end = (len(board[0][0])-1,len(board[0])-1)
true_end = (end[0],end[1]+1)

curr_time = 0
for part in range(3):
    seen = set() #pos
    initial = (true_end, curr_time) if part == 1 else ((0, -1), curr_time)
    queue = deque([initial])

    while queue:
        pos,t = queue.popleft()
        x,y = pos
        # print(pos,t)

        if t != curr_time:
            # print(t)
            seen = set()
            curr_time = t
            board = update_board(board)

        if (part != 1 and pos == end) or (part == 1 and pos == (0,0)):
            print(part,t+1) #next turn guaranteed exit
            curr_time += 1
            board = update_board(board)
            break

        # print(board[0])
        for nxt in neighbours(pos):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt,t+1))