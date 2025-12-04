import sys
import collections
from collections import deque
from functools import lru_cache, cache, cmp_to_key

with open(sys.argv[1], 'r') as f:
    lines = list(map(str.strip, f.readlines()))

current = 50
count = 0
for line in lines:
    d = line[0]
    x = int(line[1:])

    delta = 1
    if d == "L":
        delta = -1

    for _ in range(x):
        current += delta
        current %= 100

        if current == 0:
            count += 1
    print(current)

print(count)
