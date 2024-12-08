from collections import defaultdict
from functools import cmp_to_key
with open('./input.txt') as f:
    data = f.read()
# print(lines)

rules, jobs = data.split('\n\n')
rules = [tuple(map(int, l.split('|'))) for l in rules.splitlines()]

jobs = [tuple(map(int, l.split(','))) for l in jobs.splitlines()]

invalid_map = defaultdict(bool)
for x, y in rules:
    invalid_map[(y, x)] = True


# check_job
# iterates over every pair of numbers in the job
# if they are in the invalid_map, we return False
def check_job(job: list[int]) -> bool:
    for i in range(len(job)):
        for j in range(i+1, len(job)):
            if invalid_map[(job[i], job[j])]:
                return False
    return True

# comparison function that is turned into a key function
def sort_job(a: int, b: int) -> int:
    if invalid_map[(a, b)]:
        return 1
    return -1


part1 = 0
part2 = 0
for job in jobs:
    # check valid
    if check_job(job):
        part1 += job[len(job)//2]
    else:
        # convert a comparison function to a key function for sorting
        # sort based on the rule comparison
        fixed_job = sorted(job, key=cmp_to_key(sort_job))
        # add the middle element
        part2 += fixed_job[len(fixed_job)//2]

print(part1)
print(part2)
