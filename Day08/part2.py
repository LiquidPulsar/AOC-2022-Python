from pathlib import Path
import numpy as np


with open(Path(__file__).parent / "input.txt") as file:
    trees = [[*map(int, line.strip())] for line in file]


def mon_chain_dists(ts):
    return [*map(build_chain_dist, ts)]


def rev_chain_dists(ts):
    return [build_chain_dist(t[::-1])[::-1] for t in ts]


def build_chain_dist(row):
    # build descending chain
    chain = [(-1, 0)]  # v x
    out = []
    for x, v in enumerate(row):
        # print(chain[0][0])
        if v > chain[0][0]:
            chain = [(v, x)]
            out.append(x)
        else:
            while v > chain[-1][0]:
                chain.pop()
            # print(v,chain)
            out.append(x - chain[-1][1])
            chain.append((v, x))
    # print(out,chain)
    return out


# print(build_chain_dist([3,0,3,7,3]))

look_left = mon_chain_dists(trees)
look_right = rev_chain_dists(trees)


def T(x):
    return [*zip(*x)]


look_up = T(mon_chain_dists(T(trees)))
look_down = T(rev_chain_dists(T(trees)))

print("trees")
print(np.array(trees))
print("left")
print(np.array(look_left))
print("right")
print(np.array(look_right))
print("down")
print(np.array(look_down))
print("up")
print(np.array(look_up))
print("final")
final = (
    np.array(look_up) * 
    np.array(look_down) * 
    np.array(look_left) * 
    np.array(look_right)
)
print(final)
print(final.max())
