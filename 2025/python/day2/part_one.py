import sys
import collections
from collections import deque
from functools import lru_cache, cache, cmp_to_key

with open(sys.argv[1], 'r') as f:
    line = f.readline()

def part1(inputs):
    line = inputs
    rs = []
    for r in line.split(','):
        left, right = map(int, r.split('-'))
        rs.append((left, right))

    total = 0
    for i in range(1, 100000):
        x = int(str(i) * 2)

        for l, r in rs:
            if l <= x <= r:
                print(x)
                total += x


    return total

def part2(inputs):
    line = inputs
    rs = []
    for r in line.split(','):
        left, right = map(int, r.split('-'))
        rs.append((left, right))

    total = 0
    s = set()
    for i in range(1, 100000):
        for j in range(2, 10):
            x = int(str(i) * j)

            for l, r in rs:
                if l <= x <= r:
                    print(x)
                    s.add(x)
                    break


    return sum(s)


res = part1(line)
print(f'Part One:')
print(res)
print(f'-----------')
res2 = part2(line)
print(f'Part Two:')
print(res2)
