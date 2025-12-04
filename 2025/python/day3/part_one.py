import sys
import collections
import time
from math import *
import heapq

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]
with open(sys.argv[1], 'r') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]
input = grid

def part_one(input):
    total = 0
    for line in input:
        N = len(line)
        largest = 0
        second = 0
        print(line)
        for i in range(N-1): # exclusive last number
        # keep track of largest
            if line[i] > largest:
                largest = line[i]
                second = line[i+1]
        # keep track of second largest strictly after largest
            second = max(second, line[i+1])
        total += int(str(largest)+str(second))

    return total


def part_two(input):
    pass

####
res = part_one(input)
print(f'Part one: {res}')
res2 = part_two(input)
print(f'Part two: {res2}')
