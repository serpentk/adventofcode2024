GRIDSIZE = 70
BYTES_TO_FALL = 1024

corrupted = set()
for _ in range(BYTES_TO_FALL):
    line = input()
    corrupted.add(tuple((int(x) for x in line.strip().split(','))))

start = (0, 0)
end = (GRIDSIZE, GRIDSIZE)
step = 0
current = {start}
visited = set()
while current and end not in current:
    newcurrent = set()
    visited.update(current)
    for x, y in current:
        newcurrent.update({(i, j)
                           for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                           if (0 <= i <= GRIDSIZE and 0 <= j <= GRIDSIZE
                               and (i, j) not in visited
                               and (i, j) not in corrupted)})
    step += 1
    current = newcurrent
print(step)
        
