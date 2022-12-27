from collections import defaultdict
from pathlib import Path
from operator import add,mul,sub,truediv,eq
from sympy import *
import re

opdict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '==': eq
}

monkeys = {}
known = {}
with open(Path(__file__).parent / "input.txt") as file:
    for line in file:
        name, rest = line.strip().split(': ',1)
        if rest.isdigit():
            known[name] = int(rest)
        else:
            monkeys[name] = re.search(r'(\w+) (.) (\w+)',rest).groups()
(a,_,b) = monkeys['root']
monkeys['root'] = (a,'-',b)
print(monkeys)
print(known)

if 'humn' in monkeys: monkeys.pop('humn')
known['humn'] = 'x'
while 'root' in monkeys:
    hitlist = []
    for name, (a,op,b) in monkeys.items():
        if a in known and b in known:
            known[name] = f'({known[a]}){op}({known[b]})'
            hitlist.append(name)
    for name in hitlist: monkeys.pop(name)
x = Symbol('x')
print(solve(eval(known['root'])))