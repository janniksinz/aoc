import sys
with open(sys.argv[1]) as f:
    lines = f.read().split('\n')
f.close()
for line in lines[:-1]:
    print(f'{line}')

# ANTINODES
"""
for every node, check in a line if we have another node.
- checking in 8 directions ([-1,0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1])
- check until the end of the matrix
calculate the two antinode spots
- go 1/2 dx, dy into the direction
- maybe there are also antinodes in between the two nodes -> go 1/3 dx, dy in between from both sides
check oob before adding the nodes
- can antinodes of a different type overlap?
- can antinodes of the same type overlap?
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def find_stations_in_line(pos1: Point) -> list(Point):
    pass


def calc_antinodes(pos1: Point, pos2: Point) -> list(Point):
    pass
