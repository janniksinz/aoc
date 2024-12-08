file = open('./input.txt')

left, right = [], []

for line in file:
    one, two = line.split()
    left.append(one)
    right.append(two)

left.sort()
right.sort()


res = 0
for left, right in zip(left, right):
    res += abs(int(left) - int(right))

print(res)
