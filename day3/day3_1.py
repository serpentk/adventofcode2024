import re
import sys

r = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

memory = ''.join(sys.stdin.readlines())
print(sum([int(x) * int(y) for x, y in r.findall(memory)]))

