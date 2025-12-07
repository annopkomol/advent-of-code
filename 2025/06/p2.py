import math
import sys

lines = sys.stdin.read().strip().split("\n")
ops = lines[-1].split()

m = len(lines)
n = len(lines[0])
numbers = [[] for _ in range(len(ops))]
k = 0
for j in range(n):
    arr = []
    s = ""
    for i in range(m - 1):
        s += lines[i][j]
    s = s.strip()
    if s != "":
        numbers[k].append(int(s))
    else:
        k += 1

ans = 0
for i, op in enumerate(ops):
    if op == "+":
        ans += sum(numbers[i])
    else:
        ans += math.prod(numbers[i])
print(ans)
