import sys

PRUNE_MOD = 16777216

def secrets(x):
    yield x % 10
    while True:
        x = ((x * 64) ^ x) % PRUNE_MOD
        x = ((x // 32) ^ x) % PRUNE_MOD
        x = ((x * 2048) ^ x) % PRUNE_MOD
        yield x % 10


changes = dict()
maxchange = 0
p0, p1, p2, p3, p4 = None, None, None, None, None
for j, line in enumerate(sys.stdin):
    occured = set()
    for i, s in zip(range(2001), secrets(int(line.strip()))):
        p0, p1, p2, p3, p4 = p1, p2, p3, p4, s
        if all(p is not None for p in (p0, p1, p2, p3, p4)):
            change = (p1 - p0, p2 - p1, p3- p2, p4 - p3)
            if change not in occured:
                changes.setdefault(change, 0)
                changes[change] += p4
                if changes[change] > maxchange:
                    maxchange = changes[change]
                occured.add(change)

print(maxchange)
