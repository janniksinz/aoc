import sys
with open(sys.argv[1]) as f:
    lines = f.read().split('\n')
f.close()

operations = ['+', '*']


def check_possible(target: int, nums: list[int], part2=False) -> bool:
    # check validity impossible
    if len(nums) == 1:
        return target == nums[0]

    num = nums.pop()
    # print(type(target), type(num))
    if target / num == target // num:
        if check_possible(target // num, nums.copy(), part2=part2):
            return True

    if target - num >= 0:
        if check_possible(target-num, nums.copy(), part2=part2):
            return True
    if not part2:
        return False
    # part 2
    target_str = str(target)
    num_str = str(num)

    if target_str.endswith(num_str) and len(target_str) > len(num_str):
        new_target = target_str[:-len(num_str)]
        if check_possible(int(new_target), nums.copy(), part2=part2):
            return True

    return False


total = 0
for line in lines[:-1]:
    target, operands = line.split(':')
    target = int(target)
    ops = list(map(int, operands.split()))

    if check_possible(target, ops, part2=True):
        total += target

print(f'part two: {total}')
