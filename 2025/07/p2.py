import sys

grid = [list(line) for line in sys.stdin.read().split("\n")]

m = len(grid)
n = len(grid[0])

cache = {}


def beam(i: int, j: int) -> int:
    if not 0 <= j < n:
        return 0
    if not 0 <= i < m:  # hit
        return 1
    if (i, j) in cache:
        return cache[(i, j)]
    v = grid[i][j]
    if v == ".":
        return beam(i + 1, j)
    elif v == "^":
        cnt = beam(i, j + 1) + beam(i, j - 1)
        cache[(i, j)] = cnt
        return cnt
    return 0


for j, loc in enumerate(grid[0]):
    if loc == "S":
        print(beam(1, j))
