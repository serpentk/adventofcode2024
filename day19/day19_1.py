import sys

def is_possible(pattern: str, towels: list[str]):
    if len(pattern) == 0:
        return True
    return any(is_possible(pattern[len(t):], towels) for t in towels if pattern.startswith(t))


towels = input().strip().split(', ')
input()
c = 0
for line in sys.stdin:
    if is_possible(line.strip(), towels):
        c += 1
print(c)
