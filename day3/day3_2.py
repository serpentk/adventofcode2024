import re
import sys

r = re.compile(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")

memory = ''.join(sys.stdin.readlines())
on = True
s = 0
for (enable, disable, x, y) in r.findall(memory):
    if enable:
        on = True
    if disable:
        on = False
    if on and x and y:
        s += int(x) * int(y)
print(s)
