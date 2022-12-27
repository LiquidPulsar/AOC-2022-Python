from collections import defaultdict
from pathlib import Path
from operator import add,mul,sub,truediv,eq
import re

opdict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '==': eq
}

class Alg:
    def __init__(self):
        # we assume no reciprocals
        self.coeffs = defaultdict(int)
        self.coeffs[1] = 1
    
    def __add__(self,other):
        print(f'({self}) + ({other})')
        if isinstance(other,Alg):
            Alg.combine(self.coeffs,other.coeffs,add)
        else:
            self.coeffs[0] += other
        return self
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __sub__(self,other):
        print(f'({self}) - ({other})')
        if isinstance(other,Alg):
            Alg.combine(self.coeffs,other.coeffs,sub)
        else:
            self.coeffs[0] -= other
        return self
    
    def __rsub__(self,other):
        return other + self*-1

    def __mul__(self,other):
        print(f'({self}) * ({other})')
        if isinstance(other,Alg):
            Alg.combine(self.coeffs,other.coeffs,mul)
        else:
            for k in self.coeffs:
                self.coeffs[k] *= other
        return self
    
    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __truediv__(self,other):
        print(f'({self}) / ({other})')
        # sourcery skip
        if isinstance(other,Alg):
            # Alg.combine(self.coeffs,other.coeffs,truediv)
            raise NotImplementedError
        else:
            for k in self.coeffs:
                self.coeffs[k] /= other
        return self

    def __str__(self):
        return " + ".join(f"{v}x^{k}" for k,v in self.coeffs.items())

    @staticmethod
    def combine(a:dict[int,int],b:dict[int,int],op):
        for k,v in b.items():
            a[k] = op(a[k]*v)
    
    def __eq__(self:'Alg',other:'Alg'):
        print(f'({self}) == ({other})')
        new = self - other
        if set(new.coeffs) <= {0,1}:
            a = new.coeffs[1]
            b = new.coeffs[0]
            print(-b/a)


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
monkeys['root'] = (a,'==',b)
# print(monkeys)
# print(known)

if 'humn' in monkeys: monkeys.pop('humn')
known['humn'] = Alg()
while 'root' in monkeys:
    hitlist = []
    for name, (a,op,b) in monkeys.items():
        if a in known and b in known:
            known[name] = opdict[op](known[a],known[b])
            hitlist.append(name)
    for name in hitlist: monkeys.pop(name)
print(known['root'])