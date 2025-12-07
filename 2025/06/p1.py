import math
import sys

lines = sys.stdin.read().strip().split("\n")
numbers = []
ops = []
for i, line in enumerate(lines):
    if i < len(lines) - 1:
        numbers.append([int(s) for s in line.split()])
    else:
        ops = line.split()

ans = 0
numbers = [list(row) for row in zip(*numbers)]
for i, op in enumerate(ops):
    if op == "+":
        ans += sum(numbers[i])
    else:
        ans += math.prod(numbers[i])
print(ans)
