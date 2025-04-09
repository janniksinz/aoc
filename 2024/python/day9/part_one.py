import sys
with open(sys.argv[1]) as f:
    s = f.read().strip()

print(s)


# build the in fact array
def build_memory(s: str):
    d = []
    id = 0
    fill = True

    for dx in s:
        dx = int(dx)
        if fill:
            # print(f'appending {dx} times {id}')
            d.extend([id]*dx)
            id += 1
        else:
            # print(f'appending {dx} spaces')
            d.extend(['.']*dx)

        fill = not fill

    # flattened = [item for sublist in d for item in sublist]
    return d


# build a dictionary of only occupied memory
def build_dict(s: str):
    d = {}
    cur = 0
    id = 0
    fill = True

    for dx in s:
        dx = int(dx)

        for i in range(0, dx):
            if fill:
                d[cur+i] = id
        cur += dx

        if fill:
            id += 1
        fill = not fill
    return d


array = ''.join(map(str, build_memory(s)))
print(f'array: {array}')

dict_ = build_dict(s)
print(f'dict: {dict_}')

pos = 0
ans = 0

# work with dict
d = dict_
while True:
    rm = max(d.keys())  # rightmost
    id = d[rm]
    del d[rm]

    while pos in d:
        pos += 1

    d[pos] = id
    if pos == rm:
        break

for k, v in d.items():
    ans += k * v

print(ans)
