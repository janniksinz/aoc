from collections import defaultdict
with open('./input.txt') as f:
    lines = f.readlines()

# creating a map of where characters are found
char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r, c))


part1 = 0
# starting from all X locations in our map
for r, c in char_map['X']:
    # check all directions
    for dr, dc in [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    ]:
        # contain the next character
        for i, char in enumerate("MAS", 1):  # starting at M (position 1)
            # print(i, char)
            # starting from the 'X',
            if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                break
        else:
            # found a word
            part1 += 1
print(part1)
