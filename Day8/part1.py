from pathlib import Path
import numpy as np


with open(Path(__file__).parent / "input.txt") as file:
    x = np.array([[*map(int,line.strip())] for line in file])

n,m = x.shape
print(n,m) #m,n ?

down = np.append(np.zeros((1,n))-1,np.maximum.accumulate(x)[:-1],0)
right = np.append(np.zeros((m,1))-1,np.maximum.accumulate(x,1)[:,:-1],1)
up = np.append(np.zeros((1,n))-1,np.maximum.accumulate(x[::-1])[:-1],0)[::-1]
left = np.append(np.zeros((m,1))-1,np.maximum.accumulate(x[:,::-1],1)[:,:-1],1)[:,::-1]

# print(x)
# print(down)
# print(right)
# print(up)
# print(left)
print(((x>down)|(x>right)|(x>up)|(x>left)).sum())