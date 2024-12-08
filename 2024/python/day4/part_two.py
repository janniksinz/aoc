from collections import defaultdict

with open('./input.txt') as f:
    lines = f.readlines()

char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r, c))


def upleft(r, c): return (r - 1, c - 1)
def upright(r, c): return (r - 1, c + 1)
def downleft(r, c): return (r + 1, c - 1)
def downright(r, c): return (r + 1, c + 1)


part2 = 0
# checking from the middle of the cross
for r, c in char_map['A']:
    # M left
    if upleft(r, c) in char_map['M']:
        if downleft(r, c) in char_map['M'] and upright(r, c) in char_map['S'] and downright(r, c) in char_map['S']:
            part2 += 1
    # M up
    if upleft(r, c) in char_map['M']:
        if upright(r, c) in char_map['M'] and downleft(r, c) in char_map['S'] and downright(r, c) in char_map['S']:
            part2 += 1
    # M right
    if upright(r, c) in char_map['M']:
        if downright(r, c) in char_map['M'] and upleft(r, c) in char_map['S'] and downleft(r, c) in char_map['S']:
            part2 += 1
    # M down
    if downleft(r, c) in char_map['M']:
        if downright(r, c) in char_map['M'] and upleft(r, c) in char_map['S'] and upright(r, c) in char_map['S']:
            part2 += 1

print(part2)
