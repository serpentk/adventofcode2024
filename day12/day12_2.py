import sys

def count_sides(sides, prev_fun):
    prev_item = prev_fun(sides[0])
    count = 1
    for side in sides:
        if prev_fun(side) != prev_item:
            count += 1
        prev_item = side
    return count


garden = [line.strip() for line in sys.stdin]
regions = []

plots = {(i, j) for i in range(len(garden)) for j in range(len(garden[0]))}
res = 0
while plots:
    x, y = plots.pop()
    cur_plant = garden[x][y]
    cur_s = 1
    cur_region = set([(x, y)])
    tops = set([(x, y)])
    bottoms = set([(x, y)])
    lefts = set([(x, y)])
    rights = set([(x, y)])
    nbrs = {(i, j ) for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            if (i, j) in plots and garden[i][j] == cur_plant}
    while nbrs:
        cur_s += len(nbrs)
        newnbrs = set()
        for nbr in nbrs:
            if (nbr[0] - 1, nbr[1]) not in cur_region:
                tops.add(nbr)
            elif (nbr[0] - 1, nbr[1]) in bottoms:
                bottoms.remove((nbr[0] - 1, nbr[1]))

            if (nbr[0] + 1, nbr[1]) not in cur_region:
                bottoms.add(nbr)
            elif (nbr[0] + 1, nbr[1]) in tops:
                tops.remove((nbr[0] + 1, nbr[1]))

            if (nbr[0], nbr[1] - 1) not in cur_region:
                lefts.add(nbr)
            elif (nbr[0], nbr[1] - 1) in rights:
                rights.remove((nbr[0], nbr[1] - 1))

            if (nbr[0], nbr[1] + 1) not in cur_region:
                rights.add(nbr)
            elif (nbr[0], nbr[1] + 1) in lefts:
                lefts.remove((nbr[0], nbr[1] + 1))
            
            cur_region.add(nbr)
            plots.remove(nbr)
            newnbrs.update([(i, j) for i, j in plots
                            if (((i == nbr[0] and abs(j - nbr[1]) == 1) or
                                 (j == nbr[1] and abs(i - nbr[0]) == 1)) and
                                garden[i][j] == cur_plant)])
        nbrs = newnbrs

    sides = 0
    tops, bottoms, lefts, rights = list(tops), list(bottoms), list(lefts), list(rights)
    tops.sort()
    bottoms.sort()
    lefts.sort(key = lambda x: (x[1], x[0]))
    rights.sort(key = lambda x: (x[1], x[0]))
    sides = (count_sides(tops, lambda x: (x[0], x[1] - 1)) +
             count_sides(bottoms, lambda x: (x[0], x[1] - 1)) +
             count_sides(lefts, lambda x: (x[0] - 1, x[1])) +
             count_sides(rights, lambda x: (x[0] - 1, x[1])))    
    res += cur_s * sides
print(res)
