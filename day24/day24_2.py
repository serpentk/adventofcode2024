import sys
from operator import or_, and_, xor


def simple_tests(n):
    inputs =  {'{}{:02d}'.format(letter, j) : 0 for letter in ('x', 'y') for j in range(45)}
    outputs = {'z{:02d}'.format(j): 0 for j in range(46)}
    for test in ((0,0, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)):
        x, y, z, z1 = test
        inputs['x{:02d}'.format(n)], inputs['y{:02d}'.format(n)] = x, y
        outputs['z{:02d}'.format(n)], outputs['z{:02d}'.format(n + 1)] = z, z1
        yield inputs, outputs
        
def step(values, gates):
    while not all([g in values for g in gates]):
        for g in gates:
            if g in values:
                continue
            if gates[g]['inputs'][0] in values and gates[g]['inputs'][1] in values:
                values[g] = gates[g]['op'](values[ gates[g]['inputs'][0]], values[gates[g]['inputs'][1]])

def exec_test(inputs, outputs, gates):
    values = inputs.copy()
    step(values, gates)
    if {k: v for k, v in values.items() if k.startswith('z')} == outputs:
        return True
    print('Got: {}'.format({k: v for k, v in values.items()
                            if k.startswith('z') and v != outputs[k]}))
    print('Expected: {}'.format({k: v for k, v in outputs.items()
                                 if k.startswith('z') and v != values[k]}))
    return False
                
def run_tests(gates):
    c = 0
    for i in range(45):
        for j, (inp, out) in enumerate(simple_tests(i)):
            if not exec_test(inp, out, gates):
                print('Failed for {} test {}---------'.format(i, j))
                c += 1
    if c > 0:
        print("{} tests failed".format(c))
    return c


values = dict()
while ':' in input():
    continue
gates = dict()
dotfile = open('day24.dot', 'w')
dotfile.write('digraph G {\n')
for line in sys.stdin:
    i1, op, i2, _, name = line.strip().split()
    if op == 'AND':
        f = and_
    elif op == 'OR':
        f = or_
    else:
        f = xor 
    gates[name] = {'inputs': (i1, i2), 'op': f, 'label': op}
    dotfile.write('  {} -> {}\n  {} -> {}\n'.format(i1, name, i2, name))
        
dotfile.write('  {\n')
for  g in gates:
    dotfile.write('    {} [label="{} {}"]\n'.format(g, g, gates[g]['label']))
dotfile.write('  }\n')    
dotfile.write('}\n')

"""
The tests will show some problematic outputs.
Then, by visualizing the scheme from the day24.dot file,
you can find and swap problematic nodes manually and run the test again.
Example:

>>> from copy import deepcopy
>>> fixed = deepcopy(gates)
>>> fixed['z38'], fixed['nbf'] = fixed['nbf'], fixed['z38']
>>> run_tests(fixed)
"""

run_tests(gates)    
