import sys
import re

SPACEWIDTH = 101
SPACEHEIGHT = 103
STEPS = 100
s = 0
tl, tr, bl, br = 0, 0, 0, 0
r = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

space = [[0] * SPACEWIDTH for _ in range(SPACEHEIGHT)]
robots = []
f = open('day14/input.txt')
for line in f:
    startx, starty, vx, vy = (int(x) for x in r.findall(line.strip())[0])
    robots.append((startx, starty, vx, vy))
    space[starty][startx] += 1


TREE_HEIGHT = 10
def guess_tree(space):
    for col in space:
        i = 0
        while i < len(col) - TREE_HEIGHT:
            for c in range(TREE_HEIGHT):
                if col[i + c] == 0:
                    i = i + c + 1
                    break
                if c == TREE_HEIGHT - 1:
                    return True
    return False
    
while True:
    if guess_tree(space):
        print(s)
        for line in space:
            print(''.join(['.' if x == 0 else '*' for x in line]))
        input()
    for i in range(len(robots)):
        posx, posy, vx, vy = robots[i]
        space[posy][posx] -= 1
        posx, posy = (posx + vx) % SPACEWIDTH, (posy + vy) % SPACEHEIGHT
        space[posy][posx] +=1
        robots[i] = posx, posy, vx, vy
    s += 1
