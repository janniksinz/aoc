
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
    matrix = []
    for line in input[:-1]:
        matrix.append([int(x) for x in line.split()])
    symbols = input[-1].split()

    R = len(matrix)
    C = len(matrix[0])

    total = 0
    # go through every column left to right
    for i in range(C):
        # print(f'Row {i}')
        ctotal = 0 if symbols[i] == '+' else 1
        for j in range(R):
            if symbols[i] == '+':
                # print(f'+ {matrix[j][i]}')
                # add from the i'th column the j'th row element
                ctotal += matrix[j][i]
            else:
                # print(f'* {matrix[j][i]}')
                ctotal *= matrix[j][i]

        total += ctotal

    return total


def part_two(input):
    cols = list(zip(*input))  # read columns

    groups = []
    group = []
    for col in cols[:-1]:  # start with last
        if set(col) == {" "}:
            groups.append(group)
            group = []
        else:
            group.append(col)

    groups.append(group)

    total = 0
    for group in groups:
        # print(group)
        # join groups with the operator into valid math operations and eval
        total += eval(group[0][-1].join(''.join(line[:-1]).strip()
                      for line in group))
    return total


res = part_one(lines)
ph = ''
print(f'Part One: {ph}')
print(f'{res}')
res2 = part_two(grid)
print(f'Part Two: {ph}')
print(f'{res2}')
