from dataclasses import dataclass
from pathlib import Path

from tqdm import tqdm, trange

@dataclass
class Node:
    val: int
    prev: "Node"
    next: "Node"

    def right1(self):
        # l s r
        #  -->
        # l r s
        left = self.prev
        right = self.next

        self.link(right.next)
        right.link(self)
        left.link(right)
        # return self

    def left1(self):
        # l s r
        #  -->
        # s l r
        left = self.prev
        right  = self.next

        left.prev.link(self)
        self.link(left)
        left.link(right)

    def link(self,other:"Node"):
        self.next = other
        other.prev = self

def printout():
    for n in lst:
        if n.val == 0:
            break
    while n.next is not lst[0]:
        print(n.val,end=' -> ')
        n = n.next
    print(n.val)

x = 811589153
# x = 1
lst:list[Node] = []
with open(Path(__file__).parent / "input.txt") as file:
    lst.append(Node(int(file.readline())*x,None,None))
    for line in file:
        new = Node(int(line)*x,lst[-1],None)
        lst[-1].next = new
        lst.append(new)
    lst[-1].next = lst[0]
    lst[0].prev = lst[-1]

l = len(lst) - 1
for _ in range(10):
    for n in tqdm(lst):
        v = n.val
        if v<0:
            for _ in range((-v)%l):
                n.left1()
        else:
            for _ in range(v%l):
                n.right1()
    printout()
printout()

for elem in lst:
    if elem.val == 0:
        break

res = 0
v = elem
for n in range(1,3001):
    v = v.next
    if not n%1000:
        res += v.val
print(res)
# lst[0].left1()
# printout()
# lst[0].right1()
# printout()
# # lst[0].left1()
# # lst[1].right1()

# printout()
# # print(lst)