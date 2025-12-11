import sys
from typing import List


def fewest_presses(
    cnt: int, state: int, i: int, target: int, switches: List[int]
) -> int:
    if state == target:
        return cnt
    if i >= len(switches):
        return sys.maxsize
    # try not pressing the switch
    res1 = fewest_presses(cnt, state, i + 1, target, switches)
    # try pressing the switch
    res2 = fewest_presses(cnt + 1, state ^ switches[i], i + 1, target, switches)
    return min(res1, res2)


lines = sys.stdin.read().strip().split("\n")
config = []
for line in lines:
    arr = line.split(" ")[:-1]
    pattern = arr[0]
    pattern = pattern.translate(str.maketrans(".#[]", "01  ")).strip()
    n = len(pattern)
    pattern = int(pattern, 2)

    switches = []
    for v in arr[1:]:
        v = v.strip("()").split(",")
        indices = [int(i.strip()) for i in v if i.strip()]
        switch = ["0"] * n
        for i in indices:
            if 0 <= i < n:
                switch[i] = "1"
        switches.append(int("".join(switch), 2))
    config.append((pattern, switches))

ans = 0
for pattern, switches in config:
    presses = fewest_presses(0, 0, 0, pattern, switches)
    ans += presses
print(ans)
