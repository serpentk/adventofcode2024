import sys

TO_SAVE = 100
CHEAT_SIZE = 20

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
    nbrs = [(x + t, y + q)
            for t in range(-CHEAT_SIZE, CHEAT_SIZE + 1)
            for q in range(-CHEAT_SIZE, CHEAT_SIZE + 1)
            if (abs(t) + abs(q) <= CHEAT_SIZE and
                (x + t, y + q) in path and
                path[(x + t, y + q)] - path[(x, y)] - (abs(t) + abs(q)) >= TO_SAVE)]
    cheats += len(nbrs)

print(cheats)
    
