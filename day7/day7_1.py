import sys

def results(values):
    if len(values) == 1:
        yield values[0]
    else:
        for r in results(values[:-1]):
            yield r + values[-1]
            yield r * values[-1]

def check_line(res, values):
    return any(res == r for r in results(values))

s = 0
for line in sys.stdin:
    res, data = line.split(': ')
    values = data.split()
    if check_line(int(res), [int(x) for x in values]):
        s += int(res)
print(s)
