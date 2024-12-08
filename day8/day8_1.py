import sys

antennas = dict()

rows, cols = 0, 0
for i, line in enumerate(sys.stdin):
    if line:
        rows += 1
        cols = len(line.strip())
    for j, c in enumerate(line.strip()):
        if c != '.':
            antennas.setdefault(c, []).append((i, j))
antinodes = set()
for freq in antennas:
    n = len(antennas[freq])
    for i in range(n - 1):
        for j in range(i + 1, n):
            a0, b0 = antennas[freq][i]
            a1, b1 = antennas[freq][j]
            for a, b in ((2 * a0 - a1, 2 * b0 - b1), (2 * a1 - a0, 2 * b1 - b0)):
                if 0 <= a < rows and 0 <= b < cols:
                    antinodes.add((a, b))
print(len(antinodes))
