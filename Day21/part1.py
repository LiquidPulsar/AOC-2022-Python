from pathlib import Path
import re

monkeys = {}
known = {}
with open(Path(__file__).parent / "input.txt") as file:
    for line in file:
        name, rest = line.strip().split(': ',1)
        if rest.isdigit():
            known[name] = int(rest)
        else:
            monkeys[name] = re.search(r'(\w+) (.) (\w+)',rest).groups()
print(monkeys)
print(known)
while 'root' in monkeys:
    hitlist = []
    for name, (a,op,b) in monkeys.items():
        if a in known and b in known:
            known[name] = eval(f"{known[a]} {op} {known[b]}")
            hitlist.append(name)
    for name in hitlist: monkeys.pop(name)
print(known['root'])