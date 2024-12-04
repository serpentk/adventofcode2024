import sys

pair = {'S': 'M', 'M': 'S'}

data = [line.strip() for line in sys.stdin]
nrows, ncols = len(data), len(data[0])
s = 0
for i in range(nrows - 2):
    for j in range(ncols - 2):
        if data[i][j] not in ('S', 'M') or data[i + 1][j + 1] != 'A':
            continue
        if data[i + 2][j + 2] != pair[data[i][j]]:
            continue
        if ((data[i + 2][j] == data[i][j] and data[i][j + 2] == pair[data[i][j]]) or
            (data[i][j + 2] == data[i][j] and data[i + 2][j] == pair[data[i][j]])):
            s += 1
print(s)
