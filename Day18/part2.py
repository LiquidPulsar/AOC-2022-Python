from pathlib import Path
from collections import defaultdict, deque

extremes = {
    'x': {'min':float('inf'),'max':float('-inf')},
    'y': {'min':float('inf'),'max':float('-inf')},
    'z': {'min':float('inf'),'max':float('-inf')}
}

space = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
seen = set()
with open(Path(__file__).parent / "input.txt") as f:
    for line in f:
        x,y,z = map(int, line.split(','))
        seen.add((x,y,z))
        space[x][y][z] = True

        if x < extremes['x']['min']: extremes['x']['min'] = x
        if x > extremes['x']['max']: extremes['x']['max'] = x
        if y < extremes['y']['min']: extremes['y']['min'] = y
        if y > extremes['y']['max']: extremes['y']['max'] = y
        if z < extremes['z']['min']: extremes['z']['min'] = z
        if z > extremes['z']['max']: extremes['z']['max'] = z

print(extremes)

def get_faces(x,y,z):
    faces = 0
    for d in (-1,1):
        if space[x+d][y][z]: faces += 1
        if space[x][y+d][z]: faces += 1
        if space[x][y][z+d]: faces += 1
    return faces

for bit in 'xyz': # leave space to rotate around
    extremes[bit]['min'] -= 1
    extremes[bit]['max'] += 1

faces = 0
queue = deque([(extremes['x']['min'],
                extremes['y']['min'],
                extremes['z']['min'])])


while queue:
    x,y,z = queue.popleft()
    print(x,y,z)
    if (x,y,z) in seen: continue
    seen.add((x,y,z))
    faces += get_faces(x,y,z)
    for d in (-1,1):
        if (x+d,y,z) not in seen and extremes['x']['min'] <= x+d <= extremes['x']['max']:
            queue.append((x+d,y,z))
        if (x,y+d,z) not in seen and extremes['y']['min'] <= y+d <= extremes['y']['max']:
            queue.append((x,y+d,z))
        if (x,y,z+d) not in seen and extremes['z']['min'] <= z+d <= extremes['z']['max']:
            queue.append((x,y,z+d))
print(faces)