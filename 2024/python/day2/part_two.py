def is_safe(report):
    n = len(report)
    is_increasing = all(0 < report[i+1] - report[i] <= 3 for i in range(n-1))
    is_decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(n-1))
    return is_increasing or is_decreasing


def is_safe_one_removed(report):
    n = len(report)

    # go through every removal possibility
    for i in range(n):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False


file = open('./input.txt')

safe_reports = 0
for line in file:
    # map applies the int function to every element from split
    arr = list(map(int, line.split()))

    if is_safe(arr) or is_safe_one_removed(arr):
        safe_reports += 1


print(f'safe: {safe_reports}')

file.close()
