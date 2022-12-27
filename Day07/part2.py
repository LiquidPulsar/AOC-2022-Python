from pathlib import Path
from textwrap import indent

HOME = Path(__file__).parent

class Folder:
    def __init__(self,parent):
        self.parent = parent
        self.storage = {}
    
    def __getitem__(self,f):
        return self.storage[f]
    
    def __setitem__(self,k,v):
        self.storage[k] = v
    
    def __contains__(self,item):
        return item in self.storage

    @property
    def size(self):
        return sum(x.size for x in self.storage.values())

    def to_str(self,name='/'):
        res = f"- {name} (dir)"
        for k,v in self.storage.items():
            res += '\n' + indent(v.to_str(k),"  ")
        return res
    
    def gather_sizes(self):
        yield self.size
        for v in self.storage.values():
            if isinstance(v,Folder):
                yield from v.gather_sizes()

class File:
    def __init__(self, size):
        self.size = size
    
    def to_str(self, name):
        return f"- {name} (file, size={self.size})"

filesys = Folder(None)
curr = filesys

with open(HOME / "input.txt") as file:
    for line in file:
        bits = line.split()
        if bits[:2] == ['$','cd']:
            if bits[2] == '/':
                curr = filesys
            elif bits[2] == '..':
                curr = curr.parent
            else:
                curr = curr[bits[2]]

        if bits[0] == 'dir':
            if bits[1] not in curr:
                curr[bits[1]] = Folder(curr)
        elif bits[0].isdigit():
            curr[bits[1]] = File(int(bits[0]))

# print(filesys.to_str())
vs = filesys.gather_sizes()
target = next(vs) - 40_000_000 #first v is the highest by default
print(target)

print(min(v for v in vs if v>=target))