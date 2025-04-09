import sys
from collections import deque

with open(sys.argv[1], 'r') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])

zeros = [(r, c) for r, row in enumerate(grid)
         for c, val in enumerate(row) if val == 0]


def count_trails(r: int, c: int) -> int:
    q = deque([(r, c)])
    summits = set()

    while q:
        r, c = q.popleft()

        # found summit
        if grid[r][c] == 9:
            summits.add((r, c))
            continue

        # BFS
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0,  1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] + 1 == grid[nr][nc]:
                q.append((nr, nc))

    # q empty
    return len(summits)


part1 = sum(count_trails(*zero) for zero in zeros)
print(part1)

print(zeros)
