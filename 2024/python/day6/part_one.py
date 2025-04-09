with open('./input.txt') as f:
    grid = list(map(str.strip, f.readlines()))
f.close()


def get_start():
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '^':
                return (r, c)


rows = len(grid)
cols = len(grid[0])
print(rows, cols)
r, c = get_start()

# walk it
visited = set()
# start walking up
dr, dc = -1, 0

while True:
    visited.add((r, c))

    # oob
    if not (0 <= r+dr < rows and 0 <= c+dc < cols):
        break  # walking out of grid

    # barrier
    if grid[r+dr][c+dc] == '#':
        # turn
        dc, dr = -dr, dc

    # walk forward
    else:
        r += dr
        c += dc

print(f'part one: {len(visited)}')
