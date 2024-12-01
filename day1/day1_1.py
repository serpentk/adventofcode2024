import sys

loc1, loc2 = [], []

for line in sys.stdin:
    l1, l2 = (int(x) for x in line.strip().split())
    loc1.append(l1)
    loc2.append(l2)

loc1.sort()
loc2.sort()

s = 0

for x, y in zip(loc1, loc2):
    s += abs(x - y)
print(s)
