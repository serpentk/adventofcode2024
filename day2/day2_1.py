import sys

safe = 0
for line in sys.stdin:
    report = [int(x) for x in line.strip().split()]
    if (all([0 < report[i] - report[i - 1] < 4 for i in range(1, len(report))]) or
        all([0 < report[i - 1] - report[i] < 4 for i in range(1, len(report))])):
        safe += 1
print(safe)
