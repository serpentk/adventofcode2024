import sys
from operator import or_, and_, xor


values = dict()

while line := input().strip():
    name, value = line.split(': ')
    values[name] = int(value)

to_wait = []    
gates = dict()
for line in sys.stdin:
    i1, op, i2, _, name = line.strip().split()
    if op == 'AND':
        f = and_
    elif op == 'OR':
        f = or_
    else:
        f = xor 
    gates[name] = {'inputs': (i1, i2), 'op': f}
    if name.startswith('z'):
        to_wait.append(name)

while not all([x in values for x in to_wait]):
    for g in gates:
        if g in values:
            continue
        if gates[g]['inputs'][0] in values and gates[g]['inputs'][1] in values:
            values[g] = gates[g]['op'](values[ gates[g]['inputs'][0]], values[gates[g]['inputs'][1]])

res = 0
base = 1
for k in sorted(to_wait):
    res += values[k] * base
    base *= 2
print(res)
    
