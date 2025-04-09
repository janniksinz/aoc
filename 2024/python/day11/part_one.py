import sys

with open(sys.argv[1], 'r') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])

print(part1)
