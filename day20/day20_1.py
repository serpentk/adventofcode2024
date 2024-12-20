import sys

TO_SAVE = 100

start = None
end = None
path = dict()
for i, line in enumerate(sys.stdin):
    for j, c in enumerate(line.strip()):
        if c == '#':
            continue
        if c == 'S':
            start = (i, j)
        elif c == 'E':
            end = (i, j)
        path[(i, j)] = None

if start is None:
    exit(1)
cur = start
i = 0
while cur != end:
    path[cur] = i
    x, y = cur
    nex = [(z, w) for z, w in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
           if (z, w) in path and path[(z, w)] is None][0]
    i += 1
    cur = nex
path[end] = i

cheats = 0
for x, y in path:
    for z, w in ((x + 2, y), (x, y + 2), (x - 2, y), (x, y - 2)):
        if (z, w) in path and path[(z, w)] - path[(x, y)] - 2 >= TO_SAVE:
            cheats += 1

print(cheats)
    
