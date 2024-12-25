import sys

def parse_object(line, symbol): # symbol is '#' for lock, '.' for key
    heights = [0] * len(line.strip())
    try:
        while line := input():
            for i, c in enumerate(line.strip()):
                if c == symbol:
                    heights[i] += 1
    except Exception:
        pass
    return heights

def parse_key(line):
    return parse_object(line, '.')

def parse_lock(line):
    return parse_object(line, '#')

def check(key, lock):
    return all([x >= y for x, y in zip(key, lock)])

keys = []
locks = []

res = 0
for line in sys.stdin:
    if all([c == '#' for c in line.strip()]):
        lock = parse_lock(line)
        locks.append(lock)
        res += len([key for key in keys if check(key, lock)])
    else:
        key = parse_key(line)
        keys.append(key)
        res += len([lock for lock in locks if check(key, lock)])
print(res)
