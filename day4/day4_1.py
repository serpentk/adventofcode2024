import re
import sys


data = [line.strip() for line in sys.stdin]
re_xmas = re.compile(r'XMAS')
re_samx = re.compile(r'SAMX')

s = 0
for line in data:
    s += len(re_xmas.findall(line)) + len(re_samx.findall(line))
for i in range(len(data[0])):
    column = ''.join([line[i] for line in data])
    s += len(re_xmas.findall(column)) + len(re_samx.findall(column))
    print(column, len(re_xmas.findall(column)) + len(re_samx.findall(column)))
for k in range(len(data) - 3):
    d1 = ''.join([data[i + k][i] for i in range(min(len(data[0]), len(data) - k))])
    d2 = ''.join([data[i + k][len(data[0]) - i - 1] for i in range(min(len(data[0]), len(data) - k))])
    s += len(re_xmas.findall(d1)) + len(re_samx.findall(d1)) + len(re_xmas.findall(d2)) + len(re_samx.findall(d2))
for k in range(1, len(data[0]) - 3):
    d1 = ''.join([data[i][i + k] for i in range(min(len(data), len(data[0]) - k))])
    d2 = ''.join([data[i][len(data[0]) - i - k - 1]
                  for i in range(min(len(data), len(data[0]) - k))])
    s += len(re_xmas.findall(d1)) + len(re_samx.findall(d1)) + len(re_xmas.findall(d2)) + len(re_samx.findall(d2))
print(s)

    
             
