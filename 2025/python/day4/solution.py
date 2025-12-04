
import sys
import collections
from collections import deque
from functools import lru_cache, cache, cmp_to_key

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))
with open(sys.argv[1], 'r') as f:
    grid = [list(line) for line in f.readlines()]
# print(lines)
# print(grid)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, 1), (1, -1)]


def part_one(input):
    m = input
    R = len(m)
    C = len(m[0])

    # check every position
    total = 0
    for x in range(R):
        for y in range(C):
            if m[x][y] == '@':

                # if a neighbor has @, count
                count = 0
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy

                    # oob + @
                    if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == '@':
                        count += 1

                # if condition is true, remove paper role
                if count < 4:
                    total += 1
    return total


def part_two(input):
    m = input
    R = len(m)
    C = len(m[0])

    # check every position
    q = deque()
    total = 0
    for x in range(R):
        for y in range(C):
            q.appendleft((x, y))
    while q:
        x, y = q.pop()
        if m[x][y] == '@':

            # if a neighbor has @, count
            count = 0
            for dx, dy in directions:
                nx, ny = x+dx, y+dy

                # oob + @
                if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == '@':
                    count += 1

            # if condition is true, remove paper role
            if count < 4:
                total += 1
                m[x][y] = '.'
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and m[nx][ny] == '@':
                        q.append((nx, ny))
    return total


res = part_one(grid)
print(f'Part One:')
print(f'{res}')
res2 = part_two(grid)
print(f'Part Two:')
print(f'{res2}')
