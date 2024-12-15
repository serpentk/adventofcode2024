from typing import List, Tuple
import sys

def move_blocks_vertically(x: int, y: int, whmap: List[str], direction: int) -> Tuple[int, int]:
    to_move = [{(x, y)}]
    while True:
        if any(whmap[i + direction][j] == '#' for i, j in to_move[-1]):
            return x, y
        if all(whmap[i + direction][j] == '.' for i, j in to_move[-1]):
            while len(to_move) > 1:
               line = to_move.pop()
               i = list(line)[0][0]
               whmap[i + direction] = ''.join([
                     whmap[i][j] if (i, j) in line else whmap[i + direction][j]
                     for j in range(len(whmap[i]))])
               whmap[i] = ''.join([
                   '.' if (i, j) in line else whmap[i][j]
                   for j in range(len(whmap[i]))])
            whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
            whmap[x + direction] = whmap[x + direction][:y] + '@' + whmap[x + direction][y + 1:]
            return x + direction, y
        newblocks = set()
        for i, j in to_move[-1]:
            if whmap[i + direction][j] == '[':
                newblocks.update({(i + direction, j), (i + direction, j + 1)})
            elif whmap[i + direction][j] == ']':
                newblocks.update({(i + direction, j), (i + direction, j - 1)})
        to_move.append(newblocks)


def move_up(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x - 1][y] == '#':
        return x, y
    elif whmap[x - 1][y] == '.':
        whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
        whmap[x - 1] = whmap[x - 1][:y] + '@' + whmap[x - 1][y + 1:]
        return x - 1, y
    else:
        return move_blocks_vertically(x, y, whmap, -1)


def move_down(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x + 1][y] == '#':
        return x, y
    elif whmap[x + 1][y] == '.':
        whmap[x] = whmap[x][:y] + '.' + whmap[x][y + 1:]
        whmap[x + 1] = whmap[x + 1][:y] + '@' + whmap[x + 1][y + 1:]
        return x + 1, y
    else:
        return move_blocks_vertically(x, y, whmap, 1)


def move_left(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x][y - 1] == '#':
        return x, y
    elif whmap[x][y - 1] == '.':
        whmap[x] = whmap[x][:y - 1] + '@.' + whmap[x][y + 1:]
        return x, y - 1
    else:
        i = y - 1
        while whmap[x][i] in ('[', ']'):
            i -= 1
        if whmap[x][i] == '#':
            return x, y
        else:
            whmap[x] = whmap[x][:i] + whmap[x][i + 1 : y] + '@.' + whmap[x][y + 1:]
            return x, y - 1


def move_right(x: int, y: int, whmap: List[str]) -> Tuple[int, int]:
    if whmap[x][y + 1] == '#':
        return x, y
    elif whmap[x][y + 1] == '.':
        whmap[x] = whmap[x][:y] + '.@' + whmap[x][y + 2:]
        return x, y + 1
    else:
        i = y + 1
        while whmap[x][i] in ('[', ']'):
            i += 1
        if whmap[x][i] == '#':
            return x, y
        else:
            whmap[x] = whmap[x][:y] + '.@' + whmap[x][y + 1 : i] + whmap[x][i + 1:]
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
    newrow = row.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')
    warehouse.append(newrow)
    j = newrow.find('@')
    if j > -1:
        robotx = i
        roboty = j
    i += 1
    row = input().strip()
    

for line in sys.stdin:
    for c in line.strip():
        # print_map(warehouse)
        # print('Moving {}: {}, {}'.format(c, robotx, roboty))
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
           if warehouse[i][j] == '[']))
