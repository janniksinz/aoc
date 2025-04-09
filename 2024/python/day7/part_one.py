import sys
with open(sys.argv[1]) as f:
    lines = f.read().split('\n')
f.close()

operations = ['+', '*']


def check_possible(target: int, nums: list[int]) -> bool:
    # check validity impossible
    if len(nums) == 1:
        return target == nums[0]
    if target < 0:
        return False

    num = nums.pop()
    if not target % num:
        if check_possible(target // num, nums.copy()):
            return True

    if target - num >= 0:
        if check_possible(target-num, nums.copy()):
            return True

    return False


total = 0
for line in lines[:-1]:
    target, operands = line.split(':')
    target = int(target)
    ops = list(map(int, operands.split()))

    if check_possible(target, ops):
        total += target

print(total)
