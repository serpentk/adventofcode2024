import sys
import heapq


def nbrs(pos, direction, maze):
    res = []
    x, y = pos
    if direction == 'E':
        res.extend([(1000, pos, 'N'), (1000, pos, 'S')])
        if maze[x][y + 1] in ('.', 'E'):
            res.append((1, (x, y + 1), 'E'))
    elif direction == 'N':
        res.extend([(1000, pos, 'E'), (1000, pos, 'W')])
        if maze[x - 1][y] in ('.', 'E'):
            res.append((1, (x - 1, y), 'N'))
    elif direction == 'W':
        res.extend([(1000, pos, 'N'), (1000, pos, 'S')])
        if maze[x][y - 1] in ('.', 'E'):
            res.append((1, (x, y - 1), 'W'))
    if direction == 'S':
        res.extend([(1000, pos, 'E'), (1000, pos, 'W')])
        if maze[x + 1][y] in ('.', 'E'):
            res.append((1, (x + 1, y), 'S'))
    return res


end = None
start = None
maze = []
for i, line in enumerate(sys.stdin):
    maze.append(line.strip())
    e = line.find('E')
    if e > -1:
        end = i, e
    s = line.find('S')
    if s > -1:
        start = i, s

curpos = start
curdir = 'E'
queue = nbrs(start, 'E', maze)
heapq.heapify(queue)
visited = dict()
while curpos != end and queue:
    score, curpos, curdir = heapq.heappop(queue)
   
    if (curpos, curdir) in visited:
        if visited[(curpos, curdir)] > score:
            visited[(curpos, curdir)] = score
        continue
    visited[(curpos, curdir)] = score
    new = nbrs(curpos, curdir, maze)
    for s, pos, direction in new:
        if (pos, direction) not in visited:
            heapq.heappush(queue, (score + s, pos, direction))

print(min([visited[x] for x in ((end, 'N'), (end, 'S'), (end, 'E'), (end, 'W')) if x in visited]))
            
            
