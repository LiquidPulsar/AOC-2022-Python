from pathlib import Path
import numpy as np

moves: dict[str,complex] = {
    'U' : 1j,
    'D' : -1j,
    'L' : -1,
    'R' : 1
}

def propagate(h:complex,t:complex):
    X,Y = int(h.real),int(h.imag)
    x,y = int(t.real),int(t.imag)

    
    if abs(X-x)>1:
        x += 1 if x<X else -1

        y += 1 if y<Y else 0 if y==Y else -1
        
    
    if abs(Y-y)>1:
        y += 1 if y<Y else -1

        x += 1 if x<X else 0 if x==X else -1
    
    return complex(x,y)

def display(seen):
    xmin,xmax = ymin,ymax = float('inf'),float('-inf')
    for v in seen:
        x,y = int(v.real), int(v.imag)
        xmin = min(x,xmin)
        ymin = min(y,ymin)

        xmax = max(x,xmax)
        ymax = max(y,ymax)
    # print(seen,xmin,ymin,xmax,ymax)

    for y in range(ymax,ymin-1,-1):
        for x in range(xmin,xmax+1):
            print(end='#' if complex(x,y) in seen else '.')
        print()

bits = [0]*10 #head 0 tail 9
seen={0}
with open(Path(__file__).parent / "input.txt") as file:
    for d,n in map(str.split,file):
        n = int(n)

        # print(f"== {d} {n} ==")
        for _ in range(n):
            h = bits[0]+moves[d]
            for i in range(1,10):
                bits[i-1] = h
                h = propagate(h,bits[i])
            bits[9] = h
            seen.add(bits[9])

            # for a,b in zip(bits,bits[1:]):
            #     if abs(a-b)>=2:
            #         print(a,b)
            # assert all(abs(a-b)<2 for a,b in zip(bits,bits[1:]))

            # display(bits)
            # print('='*9)

# display(seen)
# print(seen)
print(len(seen))