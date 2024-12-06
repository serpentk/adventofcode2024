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
while -1 < pos[0] < len(labmap) and -1 < pos[1] < len(labmap[0]):
    visited.add(pos)
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

print(len(visited))
    
