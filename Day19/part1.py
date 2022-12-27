from pathlib import Path
import re

TMAX = 24
blue1 = [(0,4,0,0),(1,2,0,0),(2,3,14,0),(3,2,0,7)]

def parse_blueprint(string:str):
    parts = string.split(':',1)[1].split(".")
    out = []
    # print(parts)
    for i,part in enumerate(parts[:-1]):
        x = [i,0,0,0]
        for bit in re.finditer(r'(\d+) (\w+)', part):
            n,name = bit.groups()
            n = int(n)
            i = ["ore","clay","obsidian","geode"].index(name)
            x[i+1] = n
        out.append(x)
    return out

# print(parse_blueprint("Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."))

# init = state(0,0,0,1,0,0,0,0,0)
def best(blueprint, o,c,b,g, ob,cb,bb,gb, t):
    res = 0
    # if t>17:
    #     print(f"ore: {o}, clay: {c}, obsidian: {b}, geode: {g}")
    #     print(f"orebot: {ob}, claybot: {cb}, obsidianbot: {bb}, geodebot: {gb}, time: {t}")
    
    for (typ,c_ore,c_clay,c_obsidian) in blueprint:
        # build towards which bot?
        curr_o,curr_c,curr_b,curr_g,curr_t = o,c,b,g,t
        while curr_t < TMAX and (curr_o < c_ore or curr_c < c_clay or curr_b < c_obsidian):
            # print('building towards',"ore clay obs geode".split()[typ], curr_t, cb)
            curr_o += ob
            curr_c += cb
            curr_b += bb
            curr_g += gb
            curr_t += 1
            # print('++', curr_o,curr_c,cb,curr_g,curr_t)
        curr_o -= c_ore
        curr_c -= c_clay
        curr_b -= c_obsidian
        curr_o += ob
        curr_c += cb
        curr_b += bb
        curr_g += gb
        curr_t += 1

        bits = [ob,cb,bb,gb]
        bits[typ] += 1

        if typ != 3 and bits[typ] > max(x[typ+1] for x in blueprint):
            # print("dodged")
            continue

        if curr_t < TMAX:
            # print('--', curr_o,curr_c,curr_b,curr_g,curr_t)
            # print(bits)
            res = max(res, best(blueprint, curr_o,curr_c,curr_b,curr_g, *(bits), curr_t))
        if curr_t == TMAX:
            res = max(res, curr_g)
    return res

b = 0
for i,blueprint in enumerate((Path(__file__).parent / "input.txt").read_text().splitlines()):
    blueprint = parse_blueprint(blueprint)
    # print(blueprint)
    v = (i+1)*best(blueprint, 0,0,0,0, 1,0,0,0, 0)
    print(v)
    b += v
print(b)