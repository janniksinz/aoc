import re
from math import prod

with open('./input.txt') as f:
    data = f.read()

instructions = re.findall(
    r"mul\(\d{1,3},\d{1,9}\)|do\(\)|don't\(\)", data)

part2 = 0
enabled = True
for inst in instructions:
    match inst:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            x, y = map(int, inst[4:-1].split(','))
            print(x, y)
            part2 += x*y

print(part2)
