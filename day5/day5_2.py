import sys
from functools import cmp_to_key

rules: dict[int, set] = {}
for line in sys.stdin:
    if len(line) < 2:
        break
    first, second = map(int, line.split('|'))
    rules.setdefault(first, set()).add(second)

def mycmp(x, y):
    if y in rules.get(x, {}):
        return -1
    if x in rules.get(y, {}):
        return 1
    return 0

s = 0
for line in sys.stdin:
    update = list(map(int, line.split(',')))
    correct = True
    for i in range(len(update)):
        if not correct:
            break
        for x in update[i:]:
            if update[i] in rules.get(x, set()):
                correct = False
                break
    if not correct:
        update.sort(key=cmp_to_key(mycmp))
        s += update[len(update) // 2]
print(s)
                
