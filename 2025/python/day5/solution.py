
import sys
import collections
from collections import deque
from functools import lru_cache, cache, cmp_to_key

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))
with open(sys.argv[1], 'r') as f:
    grid = [list(line) for line in f.readlines()]
with open(sys.argv[1], 'r') as f:
    content = f.read()
    blocks = content.split('\n\n')
# print(lines)
# print(grid)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, 1), (1, -1)]


def part_one(input):
    count = 0
    ranges = input[0].split('\n')
    ranges = [range.split('-') for range in ranges]
    ranges = [[int(x), int(y)] for x, y in ranges]
    ids = input[1].split('\n')
    ids = [int(id) for id in ids if id != '']

    # check ids
    for id in ids:
        for x, y in ranges:
            if x <= id <= y:
                count += 1
                break

    return count


def part_two(input):
    ranges = input[0].split('\n')
    ranges = [range.split('-') for range in ranges]
    ranges = [[int(x), int(y)] for x, y in ranges]
    ranges.sort()

    c = collections.Counter()

    for s, e in ranges:
        c[s] += 1
        c[e+1] -= 1

    prev = float('-inf')
    current = 0
    total = 0
    for k in sorted(c.keys()):
        p = current
        current += c[k]

        if p == 0:
            prev = k
            continue

        total += k - prev
        prev = k

    return total


res = part_one(blocks)
ph = ''
print(f'Part One: {ph}')
print(f'{res}')
res2 = part_two(blocks)
print(f'Part Two: {ph}')
print(f'{res2}')
