import sys
from functools import cache

with open(sys.argv[1], 'r') as f:
    stones = list(map(int, f.read().strip().split(" ")))

# for i in range(75):
#    new_stones = []
#    for stone in stones:
#        if stone == 0:
#            new_stones.append(1)
#    print        elif len(str(stone)) % 2 == 0:
#            stone_len = len(str(stone))
#            left = str(stone)[:stone_len//2]
#            right = str(stone)[stone_len//2:]
#            new_stones.append(int(left))
#            new_stones.append(int(right))
#        else:
#            new_stones.append(stone*2024)
#
#    stones = new_stones
#    print(i, len(stones))


@cache
def count_stones(val: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    if val == 0:
        return count_stones(1, blinks-1)

    str_val = str(val)
    len_str_val = len(str_val)
    if len_str_val % 2 == 0:
        return (
            count_stones(int(str_val[:len_str_val//2]), blinks-1)
            + count_stones(int(str_val[len_str_val//2:]), blinks-1)
        )

    return count_stones(val * 2024, blinks - 1)

    print(len(stones))


part1 = sum(count_stones(s, 25) for s in stones)
print(f'Part1: {part1}')

part2 = sum(count_stones(s, 75) for s in stones)
print(f'Part2: {part2}')
