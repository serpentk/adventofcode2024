import re
import sys


re_a = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
re_b = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
re_prize = re.compile(r'Prize: X=(\d+), Y=(\d+)')

cost = 0
for line in sys.stdin:
    ax, ay = (int(x) for x in re_a.findall(line)[0])
    bx, by = (int(x) for x in re_b.findall(input().strip())[0])
    prize_x, prize_y  = (int(x) for x in re_prize.findall(input().strip())[0])
    det = ax * by - bx * ay
    assert det != 0
    a = (prize_x * by - prize_y * bx) // det
    b = (-prize_x * ay + prize_y * ax) // det
    if a <= 100 and b <= 100 and a * ax + b * bx == prize_x and a * ay + b * by == prize_y:
        cost += a * 3 + b
    try:
        input()
    except Exception:
        pass
print(cost)
    
