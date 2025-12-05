import sys

lines = sys.stdin.read().splitlines()
grid = [[pos == "@" for pos in line] for line in lines]

col = len(grid)
row = len(grid[0])


d = [-1, 0, 1]
ans = 0


def has_roll(i: int, j: int) -> bool:
    if not 0 <= i < row or not 0 <= j < col:
        return False
    return grid[i][j]


def cnt_adj(i: int, j: int) -> int:
    cnt = 0
    for di in d:
        for dj in d:
            if di == 0 and dj == 0:
                continue
            if has_roll(i + di, j + dj):
                cnt += 1
    return cnt


def remove(i: int, j: int):
    global ans
    if not has_roll(i, j):
        return

    cnt = cnt_adj(i, j)
    if cnt >= 4:
        return

    grid[i][j] = False
    ans += 1
    for di in d:
        for dj in d:
            remove(i + di, j + dj)


for i in range(row):
    for j in range(col):
        remove(i, j)


print(ans)
