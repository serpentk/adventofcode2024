stones = [int(x) for x in input().strip().split()]

cache = dict()

def count_stones(stone, blinks):
    cached = cache.get((stone, blinks))
    if cached:
        return cached
    if blinks == 0:
        res = 1
    elif stone == 0:
        res = count_stones(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        stone1 = int(str(stone)[:len(str(stone)) // 2])
        stone2 = int(str(stone)[len(str(stone)) // 2:])
        res = count_stones(stone1, blinks - 1) + count_stones(stone2, blinks - 1)
    else:
        res = count_stones(stone * 2024, blinks - 1)
    cache[(stone, blinks)] = res
    return res
        
print(sum([count_stones(s, 75) for s in stones]))
