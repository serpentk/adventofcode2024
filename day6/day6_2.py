import sys

guardx, guardy = -1, -1
labmap = []
for i, line in enumerate(sys.stdin):
    if guardx == -1:
        guardx = line.find('^')
        guardy = i
    labmap.append(line)

visited = set()
nextdir = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
direction = '^'

pos = (guardy, guardx)
path = []
while -1 < pos[0] < len(labmap) and -1 < pos[1] < len(labmap[0]):
    visited.add(pos)
    path.append((pos, direction))
    if direction == '^':
        nextpos = pos[0] - 1, pos[1]
    elif direction == '>':
        nextpos = pos[0], pos[1] + 1
    elif direction == 'v':
        nextpos = pos[0] + 1, pos[1]
    else:
        nextpos = pos[0], pos[1] - 1
    if -1 < nextpos[0] < len(labmap) and -1 < nextpos[1] < len(labmap[0]) and labmap[nextpos[0]][nextpos[1]] == '#':
        direction = nextdir[direction]
    else:
        pos = nextpos
   
s = 0
found = set()
for i, (p, d) in enumerate(path[1:]):
    if p in found:
        continue
    found.add(p)
    pos, direction = path[i]
    v = set(path[:i])
    labmap[p[0]] = labmap[p[0]][:p[1]] + '0' + labmap[p[0]][p[1] + 1:]
    while -1 < pos[0] < len(labmap) and -1 < pos[1] < len(labmap[0]):
        if (pos, direction) in v:
            s += 1
            break
        v.add((pos, direction))
        if direction == '^':
            nextpos = pos[0] - 1, pos[1]
        elif direction == '>':
            nextpos = pos[0], pos[1] + 1
        elif direction == 'v':
            nextpos = pos[0] + 1, pos[1]
        else:
            nextpos = pos[0], pos[1] - 1
        if (-1 < nextpos[0] < len(labmap) and -1 < nextpos[1] < len(labmap[0]) and
            labmap[nextpos[0]][nextpos[1]] in ('#', '0')):
            direction = nextdir[direction]
        else:
            pos = nextpos
    labmap[p[0]] = labmap[p[0]][:p[1]] + '.' + labmap[p[0]][p[1] + 1:]
print(s)
    
