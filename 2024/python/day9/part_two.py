import sys
with open(sys.argv[1]) as f:
    s = f.read().strip()

print(s)
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
    print(f'returning disk: \n{disk}')
    return disk


disk = build()
empties = [i for i, val in enumerate(disk) if val == -1]

isfile = True
files = {}
spaces = []
ptr = 0
for i, size in enumerate(data):
    # add file
    if isfile:
        files[i//2] = (ptr, size)
    # add empty space
    else:
        spaces.append((ptr, size))

    isfile = not isfile
    ptr += size

print(f'files: \n{files}\nspaces: \n{spaces}\n')

for fid in reversed(files):
    pos, file_size = files[fid]
    print(size)

    # finding the first space on the right
    space_id = 0
    while space_id < len(spaces):
        space_loc, space_size = spaces[space_id]
        if space_size == file_size:
            files[fid] = (space_loc, file_size)
            spaces.pop(space_id)
