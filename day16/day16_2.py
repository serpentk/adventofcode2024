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
queue = [(0, start, 'E', None)]
visited = dict()
prev = None
while queue:
    score, curpos, curdir, prev = heapq.heappop(queue)
   
    if (curpos, curdir) in visited:
        if visited[(curpos, curdir)][0] == score:
            visited[(curpos, curdir)][1].add(prev)
            visited[(curpos, curdir)] = score,  visited[(curpos, curdir)][1]
        elif visited[(curpos, curdir)][0] > score:
            visited[(curpos, curdir)] = score, {prev}
        continue
    visited[(curpos, curdir)] = score, {prev}
    new = nbrs(curpos, curdir, maze)
    for s, pos, direction in new:
        if (pos, direction) not in visited:
            heapq.heappush(queue, (score + s, pos, direction, (curpos, curdir)))

best_score = min([visited[x][0]
                  for x in ((end, 'N'), (end, 'S'), (end, 'E'), (end, 'W'))
                  if x in visited])      
all_tiles = set()
cur_tiles = {x for x in ((end, 'N'), (end, 'S'), (end, 'E'), (end, 'W'))
             if x in visited and visited[x][0] == best_score}

while cur_tiles:
    all_tiles.update(cur_tiles)
    cur_tiles = {tile for tile in set.union(*(visited[t][1] for t in cur_tiles))
                 if tile is not None}
print(len({tile[0] for tile in all_tiles}))

            
