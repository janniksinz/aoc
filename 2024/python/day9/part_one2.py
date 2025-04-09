import sys
with open(sys.argv[1]) as f:
    s = f.read().strip()

# print(s)
data = list(map(int, s))


def build():
    # build data
    disk = []
    for i in range(0, len(data), 2):
        # print(f'extending: {data[i]} {data[i] * [i//2]}')
        disk.extend(data[i] * [i//2])  # frequency * [id]

        # extend the list with empty space
        if i + 1 < len(data):
            # print(f'extending: {data[i+1]} {data[i + 1] * [-1]}')
            disk.extend(data[i + 1] * [-1])  # frequency * [-1]
    # print(f'returning disk: \n{disk}')
    return disk


disk = build()
empties = [i for i, val in enumerate(disk) if val == -1]

# two pointer
left, right = 0, len(disk)-1
while left < right:
    if disk[left] != -1:
        left += 1
        continue

    # space available shift r
    while disk[right] == -1:
        disk[right] = 0
        right -= 1

    disk[left] = disk[right]
    disk[right] = 0
    left += 1
    right -= 1

print(f'left: {left}, right: {right}')
# print(f'new disk: \n{disk}')

# sum_ = sum([i*val for i, val in enumerate(disk[:right])])

sum_ = sum(i*val for i, val in enumerate(disk))

print(sum_)
