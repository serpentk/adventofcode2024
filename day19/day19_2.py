import sys
import functools

@functools.cache
def num_arrangements(pattern: str, towels):
    if len(pattern) == 0:
        return 1
    return sum(num_arrangements(pattern[len(t):], towels) for t in towels if pattern.startswith(t))


towels = tuple(input().strip().split(', '))
input()
c = 0
print(sum(num_arrangements(line.strip(), towels) for line in sys.stdin))
