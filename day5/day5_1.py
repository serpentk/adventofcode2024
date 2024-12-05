import sys

rules: dict[int, set] = {}
for line in sys.stdin:
    if len(line) < 2:
        break
    first, second = map(int, line.split('|'))
    rules.setdefault(first, set()).add(second)

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
    if correct:
        s += update[len(update) // 2]
print(s)
                
