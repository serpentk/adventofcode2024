import sys


def is_perfectly_safe(report):
    return (all([0 < report[i] - report[i - 1] < 4 for i in range(1, len(report))]) or
        all([0 < report[i - 1] - report[i] < 4 for i in range(1, len(report))]))

def is_safe(report):
    if is_perfectly_safe(report):
        return True
    for i in range(len(report)):
        if is_perfectly_safe(report[:i] + report[i + 1:]):
            return True
    return False
                   

safe = 0
for line in sys.stdin:
    report = [int(x) for x in line.strip().split()]
    if is_safe(report):
        safe += 1
print(safe)
