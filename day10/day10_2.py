import sys
data = [[int(x) for x in line.strip()] for line in sys.stdin]
scores = [[1 if data[i][j] == 9 else 0 for j in range(len(data[0]))] for i in range(len(data))]
for k in range(8, -1, -1):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != k:
                continue
            nbrs = [scores[x][y]
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
                    if 0 <= x < len(data) and 0 <= y < len(data[0]) and data[x][y] == k + 1]
            scores[i][j] = sum(nbrs)

print(sum([scores[i][j]
           for i in range(len(data))
           for j in range(len(data[0]))
           if data[i][j] == 0
           ]))
