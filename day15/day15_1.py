from typing import List, Tuple
import sys


def move_up(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x - 1][y] == '#':
        return x, y
    elif whmap[x - 1][y] == '.':
        whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
        whmap[x - 1] = whmap[x - 1][:y] + '@' + whmap[x - 1][y + 1:]
        return x - 1, y
    else:
        i = x - 1
        while whmap[i][y] == 'O':
            i -= 1
        if whmap[i][y] == '#':
            return x, y
        else:
            whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
            whmap[i]= whmap[i][:y] + 'O' + whmap[i][y + 1:] 
            whmap[x - 1] = whmap[x - 1][:y] + '@' + whmap[x - 1][y + 1:]
            return x - 1, y


def move_down(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x + 1][y] == '#':
        return x, y
    elif whmap[x + 1][y] == '.':
        whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
        whmap[x + 1] = whmap[x + 1][:y] + '@' + whmap[x + 1][y + 1:]
        return x + 1, y
    else:
        i = x + 1
        while whmap[i][y] == 'O':
            i += 1
        if whmap[i][y] == '#':
            return x, y
        else:
            whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
            whmap[i]= whmap[i][:y] + 'O' + whmap[i][y + 1:] 
            whmap[x + 1] = whmap[x + 1][:y] + '@' + whmap[x + 1][y + 1:]
            return x + 1, y


def move_left(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x][y - 1] == '#':
        return x, y
    elif whmap[x][y - 1] == '.':
        whmap[x] = whmap[x][:y - 1] + '@.' + whmap[x][y + 1:]
        return x, y - 1
    else:
        i = y - 1
        while whmap[x][i] == 'O':
            i -= 1
        if whmap[x][i] == '#':
            return x, y
        else:
            whmap[x] = whmap[x][:i] + (y - i - 1) * 'O' + '@.' + whmap[x][y + 1:]
            return x, y - 1


def move_right(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x][y + 1] == '#':
        return x, y
    elif whmap[x][y + 1] == '.':
        whmap[x] = whmap[x][:y] + '.@' + whmap[x][y + 2:]
        return x, y + 1
    else:
        i = y + 1
        while whmap[x][i] == 'O':
            i += 1
        if whmap[x][i] == '#':
            return x, y
        else:
            whmap[x] = whmap[x][:y] + '.@' + (i - y - 1) * 'O' + whmap[x][i + 1:]
            return x, y + 1


def print_map(whmap: List[str]) -> None:
    for line in whmap:
        print(line)
    print('----------------')
        
warehouse: List[str] = []
row = input().strip()
i = 0
robotx, roboty = 0, 0
while len(row) > 0:
    warehouse.append(row)
    x = row.find('@')
    if x > -1:
        robotx = x
        roboty = i
    i += 1
    row = input().strip()
    

for line in sys.stdin:
    for c in line.strip():
        # print_map(warehouse)
        # print('Moving {}'.format(c))
        if c == '^':
            robotx, roboty = move_up(robotx, roboty, warehouse)
        elif c == 'v':
            robotx, roboty = move_down(robotx, roboty, warehouse)
        elif c == '>':
            robotx, roboty = move_right(robotx, roboty, warehouse)
        elif c == '<':
            robotx, roboty = move_left(robotx, roboty, warehouse)
# print_map(warehouse)
print(sum([100 * i + j
           for i in range(len(warehouse))
           for j in range(len(warehouse[0]))
           if warehouse[i][j] == 'O']))
