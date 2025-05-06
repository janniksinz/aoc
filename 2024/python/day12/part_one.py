import sys
from collections import deque

with open(sys.argv[1], 'r') as f:
    grid = list(map(str.strip, f.readlines()))

rows = len(grid)
cols = len(grid[0])

regions = []
seen = set()


def perimeter(region: set[tuple[int]]) -> int:
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    total = 0
    for r, c in region:
        num_neighbors = len(
            [1 for dr, dc in directions if (r+dr, c+dc) in region]
        )
        total += 4-num_neighbors
    return total


for row in range(rows):
    # go through every position
    for col in range(cols):
        if (row, col) in seen:
            continue

        # new region, add it to queue
        region = set()
        q = deque([(row, col)])

        # find all positions that belong to the region
        while q:
            r, c = q.popleft()
            region.add((r, c))
            seen.add((r, c))
            directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (
                    # not seen
                    (nr, nc) not in seen and
                    # bounds
                    0 <= nr < rows and
                    0 <= nc < cols and
                    # belongs to region
                    grid[nr][nc] == grid[r][c]
                ):
                    q.append((nr, nc))
                    seen.add((nr, nc))
        # q empty -> discovered entire region
        # print(region)
        regions.append(region)
        seen |= region

        # store region somewhere

# go through every region and calculate area and circumference
total = 0
# AREA
for i, region in enumerate(regions):
    area = len(region)
    cir = perimeter(region)
    print(f'{i}: area: {area}, perimeter: {cir}')
    total += area*cir


print(total)
