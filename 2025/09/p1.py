import sys

lines = sys.stdin.read().strip().split("\n")
pos_list = [(int(x), int(y)) for x, y in (line.split(",") for line in lines)]

pos_list.sort()
n = len(pos_list)
max_area = 0
for i in range(n):
    x1, y1 = pos_list[i]
    for j in range(i + 1, n):
        x2, y2 = pos_list[j]
        if x1 != x2 and y1 != y2:
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)
print(max_area)
