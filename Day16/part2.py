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
import time
print(dfs('AA',0,0,relevant))

v = float('-inf')
for r in range(8):
    print(r)
    t = time.perf_counter()
    for comb in combinations(relevant,r):
        rest = relevant - set(comb)
        # print(rest)
        v = max(v,dfs('AA',4,0,rest)+dfs('AA',4,0,frozenset(comb)))
    print(time.perf_counter()-t)
print(v)