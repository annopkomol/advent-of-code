import sys
from typing import List


def find_max_jol(bank: List[int]):
    n = len(bank)
    x = max(bank)
    ix = bank.index(x)

    if ix == n - 1:
        y = max(bank[:-1])
        return (y * 10) + x
    else:
        y = max(bank[ix + 1 :])
        return (x * 10) + y


lines = sys.stdin.read().splitlines()
banks = [[int(bat) for bat in line] for line in lines]

ans = 0
for bank in banks:
    ans += find_max_jol(bank)

print(ans)
