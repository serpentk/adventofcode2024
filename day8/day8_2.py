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
            points = [(a0 + k *(a1 - a0), b0 + k *(b1 - b0))
                      for k in range(-max(rows, cols), max(rows, cols) + 1)]
            antinodes.update([(a, b) for (a, b) in points if 0 <= a < rows and 0 <= b < cols])
print(len(antinodes))
