from collections import defaultdict, deque
from itertools import combinations, product
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
relevant = frozenset({k for k,v in flows.items() if v})
print(relevant)
# print(links)
from functools import lru_cache

# @lru_cache(maxsize=None)
def dfs(pos,time,flow,relevant):
    # print(pos,time,flow,activated)
    if time > 30: return float('-inf')
    if time == 30: return flow

    flow+=(30-time)*flows[pos]
    relevant = relevant - {pos} # activate
    return max((dfs(k,
                time+links[pos][k]+1,
                flow,
                relevant) for k in relevant),default=flow)

# @lru_cache(maxsize=None)
def dfs2(p1,p2,t1,t2,f,relevant):
    # print(p1,p2,t1,t2,f,relevant)
    if t2<t1:
        p1,p2 = p2,p1
        t1,t2 = t2,t1

    if t1==30: return f

    f+=(30-t1)*flows[p1]
    relevant = relevant - {p1}
    return max((dfs2(k,
                p2,
                t1+links[p1][k]+1,
                t2,
                f,
                relevant) for k in relevant if t1+links[p1][k]<=29),default=f)

import time
t = time.perf_counter()
n = 8
print(dfs2('AA','AA',n,n,0,relevant))
print(time.perf_counter()-t)