import re
from math import prod

with open('./input.txt') as f:
    data = f.read()

# mul(123, 123)
# capture groups
pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
# print(pairs)

# mapping to int -> calc product of iterable
values = [prod(map(int, val)) for val in pairs]
print(sum(values))
