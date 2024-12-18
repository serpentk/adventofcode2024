import sys

GRIDSIZE = 70
BYTES_TO_FALL = 1024

corrupted_list = [tuple((int(x) for x in line.strip().split(','))) for line in sys.stdin]

start = (0, 0)
end = (GRIDSIZE, GRIDSIZE)
corrupted = set(corrupted_list[: BYTES_TO_FALL])

for byte in corrupted_list[BYTES_TO_FALL:]:
    current = {start}
    visited = set()
    corrupted.add(byte)
    while current and end not in current:
        newcurrent = set()
        visited.update(current)
        for x, y in current:
            newcurrent.update({(i, j)
                               for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                               if (0 <= i <= GRIDSIZE and 0 <= j <= GRIDSIZE
                                   and (i, j) not in visited
                                   and (i, j) not in corrupted)})
            current = newcurrent
    if end not in current:
        print(byte)
        break
        
