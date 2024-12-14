import sys
import re

SPACEWIDTH = 101
SPACEHEIGHT = 103
STEPS = 100
s = 0
tl, tr, bl, br = 0, 0, 0, 0
r = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
for line in sys.stdin:
    startx, starty, vx, vy = (int(x) for x in r.findall(line.strip())[0])
    px, py = (startx + STEPS * vx) % SPACEWIDTH, (starty + STEPS * vy) % SPACEHEIGHT
    if px < SPACEWIDTH // 2 and py < SPACEHEIGHT // 2:
        tl += 1
    elif px < SPACEWIDTH // 2 and py > SPACEHEIGHT // 2:
        bl += 1
    elif px > SPACEWIDTH // 2 and py > SPACEHEIGHT // 2:
        br += 1
    elif px > SPACEWIDTH // 2 and py < SPACEHEIGHT // 2:
        tr += 1

print(tl * tr * br * bl)
