from collections import defaultdict
with open('./ex.txt') as f:
    data = f.read()
# print(lines)

rules, jobs = data.split('\n\n')
rules = [tuple(map(int, l.split('|'))) for l in rules.splitlines()]

jobs = [tuple(map(int, l.split(','))) for l in jobs.splitlines()]

invalid_map = defaultdict(bool)
for x, y in rules:
    invalid_map[(y, x)] = True


def check_job(job):
    for i in range(len(job)):
        for j in range(i+1, len(job)):
            if invalid_map[(job[i], job[j])]:
                return 0
    return job[len(job)//2]


part1 = 0
for job in jobs:
    # check valid
    part1 += check_job(job)

print(part1)
