import sys

with open(sys.argv[1], 'r') as f:
    stones = list(map(int, f.read().strip().split(" ")))

for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_len = len(str(stone))
            left = str(stone)[:stone_len//2]
            right = str(stone)[stone_len//2:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(stone*2024)

    stones = new_stones

print(len(stones))
