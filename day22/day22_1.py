import sys

PRUNE_MOD = 16777216

def secrets(x):
    while True:
        x = ((x * 64) ^ x) % PRUNE_MOD
        x = ((x // 32) ^ x) % PRUNE_MOD
        x = ((x * 2048) ^ x) % PRUNE_MOD
        yield x

res = 0
for line in sys.stdin:
    for i, s in enumerate(secrets(int(line.strip()))):
        if i == 1999:
            res += s
            break
print(res)
