import sys
from typing import List


def find_max_jol(bank: List[int], k: int = 12):
    stack = []
    n = len(bank)
    drop_budget = n - k

    if drop_budget < 0:
        return 0

    for digit in bank:
        while drop_budget > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop_budget -= 1
        stack.append(digit)

    res = 0
    for digit in stack[:k]:
        res = (res * 10) + digit
    return res


lines = sys.stdin.read().splitlines()
banks = [[int(bat) for bat in line] for line in lines]

ans = 0
for bank in banks:
    ans += find_max_jol(bank)

print(ans)
