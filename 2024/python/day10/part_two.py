import sys
from collections import deque

with open(sys.argv[1], 'r') as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

rows = len(grid)
cols = len(grid[0])

zeros = [(r, c) for r, row in enumerate(grid)
         for c, val in enumerate(row) if val == 0]


# number of unique trails that lead from a trailhead to any 9s reachable
def count_trails(r: int, c: int) -> int:
    q = deque([(r, c)])
    count = 0

    while q:
        r, c = q.popleft()

        # found summit
        if grid[r][c] == 9:
            count += 1
            continue

        # BFS
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0,  1)]:
            nr, nc = r + dr, c + dc
            if (  # checking OutOfBounds && increasing numbers
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[r][c] + 1 == grid[nr][nc]
            ):
                q.append((nr, nc))

    # q empty
    return count


part2 = sum(count_trails(*zero) for zero in zeros)
print(part2)

print(zeros)
