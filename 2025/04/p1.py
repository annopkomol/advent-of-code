import sys

lines = sys.stdin.read().splitlines()
grid = [[pos == "@" for pos in line] for line in lines]

col = len(grid)
row = len(grid[0])


def has_roll(i: int, j: int) -> bool:
    if not 0 <= i < row or not 0 <= j < col:
        return False
    return grid[i][j]


def can_access(i: int, j: int) -> bool:
    if not grid[i][j]:
        return False
    d = [-1, 0, 1]
    cnt = 0
    for di in d:
        for dj in d:
            if di == 0 and dj == 0:
                continue
            if has_roll(i + di, j + dj):
                cnt += 1

    return cnt < 4


ans = 0
for i in range(row):
    for j in range(col):
        v = can_access(i, j)
        if v:
            ans += 1


print(ans)
