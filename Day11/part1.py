from pathlib import Path
import re
from functools import reduce
from operator import mul

def product(i):
    return reduce(mul,i,1)

DATA = (Path(__file__).parent / "input.txt").read_text()
monkey_pattern = re.compile(
    r"Monkey (?P<num>\d+):\n"
    r"  Starting items: (?P<items>(\d+, )*\d+)\n"
    r"  Operation: new = (?P<op>[^\n]+)\n"
    r"  Test: divisible by (?P<test>\d+)\n"
    r"    If true: throw to monkey (?P<t_monk>\d+)\n"
    r"    If false: throw to monkey (?P<f_monk>\d+)"
)

class Monkey:
    monkey_dict:dict[int,"Monkey"] = {}

    def __init__(self, dct:dict[str,str]):
        num,items,op,test,t_monk,f_monk = dct.values()
        self.num = int(num)
        self.items = [*map(int,items.split(', '))]
        self.op = lambda old: eval(op,{'old':old})
        self.test = int(test)
        self.t_monk = int(t_monk)
        self.f_monk = int(f_monk)
        self.inspections = 0
        Monkey.monkey_dict[self.num] = self

    def play(self):
        # print(f"Monkey {self.num}:")
        for item in self.items:
            self.inspections += 1
            # print(f"  Monkey inspects an item with a worry level of {item}")
            item:int = self.op(item)
            # print(f"  Worry level goes to {item}")
            item //= 3
            # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}")
            if item % self.test: # f
                # print(f"    Current worry level is not divisible by {self.test}")
                self.throw(item, self.f_monk)
            else: # t
                # print(f"    Current worry level is divisible by {self.test}")
                self.throw(item, self.t_monk)
        self.items = []

    def throw(self,item,id):
        # print(f"    Item with worry level {item} is thrown to monkey {id}")
        Monkey.monkey_dict[id].items.append(item)

for monkey in re.finditer(monkey_pattern, DATA):
    Monkey(monkey.groupdict())

# print(Monkey.monkey_dict)
for _ in range(20):
    for monkey in Monkey.monkey_dict.values():
        monkey.play()
for monkey in Monkey.monkey_dict.values():
    print(monkey.items)

top2 = sorted((monkey.inspections for monkey in Monkey.monkey_dict.values()),reverse=True)[:2]
print(product(top2))