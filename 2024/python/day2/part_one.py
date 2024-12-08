file = open('./input.txt')


save_reports = 0
for line in file:
    report = list(map(int, line.split()))
    # get the len of the report
    n = len(report)

    is_increasing = all(0 < report[i+1] - report[i] <= 3 for i in range(n-1))
    is_decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(n-1))

    if is_increasing or is_decreasing:
        save_reports += 1

print(save_reports)

file.close()
