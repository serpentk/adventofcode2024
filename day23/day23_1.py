import sys

network = dict()
for line in sys.stdin:
    x, y = line.strip().split('-')
    network.setdefault(x, set()).add(y)
    network.setdefault(y, set()).add(x)

s = 0
found = set()
for item in network:
    if item[0] != 't':
        continue
    for x in network[item]:
        for y in network[item]:
            if x in network[y]:
                found.add(tuple(sorted([item, x, y])))
print(len(found))
    
    
