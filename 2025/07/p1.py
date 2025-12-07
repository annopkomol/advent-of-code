import sys
from collections import deque

grid = [list(line) for line in sys.stdin.read().split("\n")]
q = deque()
for j, loc in enumerate(grid[0]):
    if loc == "S":
        q.append((0, j))

m = len(grid)
n = len(grid[0])

hit = set()
while q:
    qlen = len(q)
    for _ in range(qlen):
        i, j = q.popleft()
        i += 1  # down
        if not 0 <= i < m:  # fall off grid
            continue
        # not hit
        if grid[i][j] == ".":
            grid[i][j] = "|"
            q.append((i, j))
        elif grid[i][j] == "^":
            hit.add((i, j))
            q.append((i - 1, j + 1))
            q.append((i - 1, j - 1))


print(len(hit))
