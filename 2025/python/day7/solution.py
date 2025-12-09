
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
    print(input)
    pass


def part_two(input):
    pass


res = part_one(grid)
ph = ''
print(f'Part One: {ph}')
print(f'{res}')
res2 = part_two(blocks)
print(f'Part Two: {ph}')
print(f'{res2}')
