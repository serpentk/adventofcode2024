stones = [int(x) for x in input().strip().split()]

for i in range(25):
    newstones = []
    for stone in stones:
        if stone == 0:
            newstones.append(1)
        elif len(str(stone)) % 2 == 0:
            newstones.extend([int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])])
        else:
            newstones.append(stone * 2024)
    stones = newstones

print(len(stones))
    
