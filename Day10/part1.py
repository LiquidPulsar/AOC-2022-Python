from pathlib import Path
import numpy as np

x=[0]*1000 #by t = cycles finished
t=0
with open(Path(__file__).parent / "input.txt") as file:
    for l in file:
        # x[t+2] += int(l[6:].strip() or 0)
        if l.strip() != "noop":
            _,v = l.split()
            v =  int(v)
            x[t+2] += v
            t+=1
        t += 1
y=[1]
y.extend(y[-1]+i for i in x[1:])
print(y[:40])

print(sum(x * y[x-1] for x in range(20,221,40)))
# print([y[x-1] for x in range(20,221,40)])