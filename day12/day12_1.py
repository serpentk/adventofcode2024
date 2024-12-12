import sys

garden = [line.strip() for line in sys.stdin]
regions = []

plots = {(i, j) for i in range(len(garden)) for j in range(len(garden[0]))}
res = 0
while plots:
    x, y = plots.pop()
    cur_plant = garden[x][y]
    cur_s = 1
    cur_p = 4
    cur_region = set([(x, y)])
    nbrs = {(i, j ) for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            if (i, j) in plots and garden[i][j] == cur_plant}
    while nbrs:
        cur_s += len(nbrs)
        newnbrs = set()
        for nbr in nbrs:
            n_common = len([(i, j) for i, j in cur_region
                            if ((i == nbr[0] and abs(j - nbr[1]) == 1) or
                                (j == nbr[1] and abs(i - nbr[0]) == 1))])
            cur_p += 4 - 2 * n_common
            cur_region.add(nbr)
            plots.remove(nbr)
            newnbrs.update([(i, j) for i, j in plots
                            if (((i == nbr[0] and abs(j - nbr[1]) == 1) or
                                 (j == nbr[1] and abs(i - nbr[0]) == 1)) and
                                garden[i][j] == cur_plant)])
        nbrs = newnbrs
    res += cur_p * cur_s
print(res)
