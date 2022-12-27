from collections import defaultdict, deque
from itertools import product
from pathlib import Path
import re

links = {}
flows = {}

with open(Path(__file__).parent / "input.txt") as file:
    for line in file:
        n,r,ns = re.match(
            r"Valve (\w+) has flow rate=(\d+); "
            r"tunnels? leads? to valves? (\w+(?:, \w+)*)",
            line).groups()
        r = int(r)
        ns = ns.split(", ")
        links[n] = ns
        flows[n] = r


def floyd_warshall(links):
    dists = defaultdict(lambda: defaultdict(lambda: float("inf")))

    for s in links:
        dists[s][s] = 0
        for e in links[s]:
            dists[s][e] = 1
    
    for k,i,j in product(links,repeat=3):
        dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    return dists


links = floyd_warshall(links)
relevant = {k for k,v in flows.items() if v}
print(relevant)
# print(links)
def dfs(pos,time,flow,activated):
    # print(pos,time,flow,activated)
    if time > 30: return float('-inf'),[]
    if time == 30: return flow,[]

    flow+=(30-time)*flows[pos]

    res = flow # do nothing
    best = [(pos,time)]
    activated = activated | {pos} # activate
    for k in relevant - activated:
        f,path = dfs(k,
                time+links[pos][k]+1,
                flow,
                activated)
        if res < f:
            res = f
            best = [(pos,time)] + path
    return res, best


import time
t = time.perf_counter()
print(dfs('AA',0,0,set()))
print(time.perf_counter()-t)