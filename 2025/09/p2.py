import sys

lines = sys.stdin.read().strip().split("\n")
pos_list = [(int(x), int(y)) for x, y in (line.split(",") for line in lines)]

pset = set(pos_list)
n = len(pos_list)

edges = []
for i in range(n):
    p1 = pos_list[i]
    p2 = pos_list[(i + 1) % n]
    edges.append((p1, p2))


def valid(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)

    for (a, b), (c, d) in edges:
        # Vertical edge
        if a == c and x_min < a < x_max:
            if not (max(b, d) < y_min or min(b, d) > y_max):
                return False
        # Horizontal edge
        if b == d and y_min < b < y_max:
            if not (max(a, c) < x_min or min(a, c) > x_max):
                return False
    return True


max_area = 0
for i in range(n):
    x1, y1 = pos_list[i]
    for j in range(i + 1, n):
        x2, y2 = pos_list[j]
        if x1 != x2 and y1 != y2:
            if not valid((x1, y1), (x2, y2)):
                continue
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)
print(max_area)
