import sys

from collections import Counter


loc1, loc2 = [], []

for line in sys.stdin:
    l1, l2 = (int(x) for x in line.strip().split())
    loc1.append(l1)
    loc2.append(l2)

c = Counter(loc2)
print(sum([x * c[x] for x in loc1]))
