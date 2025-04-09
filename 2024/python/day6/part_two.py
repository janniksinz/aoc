with open('./input.txt') as f:
    grid = list(map(list, map(str.strip, f.readlines())))
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


start_r, start_c = get_start()


def check_for_loop():
    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()

    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r+dr < rows and 0 <= c+dc < cols):
            return False
        if grid[r+dr][c+dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc


part2 = 0
for ro in range(rows):
    for co in range(cols):
        if grid[ro][co] != '.':
            continue
        grid[ro][co] = '#'
        if check_for_loop():
            part2 += 1
        grid[ro][co] = '.'


print(f'part two: {part2}')
