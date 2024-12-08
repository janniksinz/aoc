from collections import defaultdict
file = open('./input.txt')

left, right = [], []
cnt_right = defaultdict(int)


for line in file:
    one, two = line.split()
    left.append(int(one))
    right.append(int(two))
    cnt_right[int(two)] += 1

file.close()

res = 0
for num in left:
    res += int(num) * cnt_right[num]

print(res)
