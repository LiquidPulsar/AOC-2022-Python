from pathlib import Path
from collections import deque

sig_map = (Path(__file__).parent / "input.txt").read_bytes().splitlines()
X,Y = len(sig_map[0])-1, len(sig_map)-1

starts = list((x,y) for y,row in enumerate(sig_map) 
            for x,v in enumerate(row) if v==ord('S') or v==ord('a'))
# print(starts)
end = next((x,y) for y,row in enumerate(sig_map) 
            for x,v in enumerate(row) if v==ord('E'))

def neighbours(x,y):
    if x>0: yield (x-1,y)
    if y>0: yield (x,y-1)

    if x<X: yield (x+1,y)
    if y<Y: yield (x,y+1)

# print(*sig_map,sep='\n')
m = float('inf')
for start in starts:
    queue = deque([(start,ord('a'),0)])
    seen = {start}

    # curr_d = -1
    while queue:
        # print(queue)
        (x,y),h,d = queue.popleft()
        # if d!=curr_d:
            # print(curr_d:=d)
        # print((x,y),h,d)
        for (new_x,new_y) in neighbours(x,y):
            v = sig_map[new_y][new_x]
            if (new_x,new_y) in seen:
                continue
            if v == ord('E'):
                if h >= ord('z')-1:
                    print('Ans:',d+1)
                    m = min(m,d+1)
                    break
            else:
                # print(h,v)
                if h >= v-1:
                    # print(new_x,new_y)
                    queue.append(((new_x,new_y),v,d+1))
                    seen.add((new_x,new_y))
        else:
            continue
        break
    else:
        print("failed")
print(m)