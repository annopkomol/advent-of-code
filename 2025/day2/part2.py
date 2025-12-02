import sys
from typing import List


def is_invalid(s: str) -> bool:
    n = len(s)
    if n < 2:
        return False

    for length in range(1, n // 2 + 1):
        if n % length == 0:
            pattern = s[:length]
            repeat_count = n // length
            if s == pattern * repeat_count:
                return True

    return False


def find_invalid_ids(first: str, last: str) -> List[int]:
    ans = []
    for v in range(int(first), int(last) + 1):
        if is_invalid(str(v)):
            ans.append(v)

    return ans


input_data = sys.stdin.read().strip()
id_ranges = []
parts = input_data.split(",")
for part in parts:
    start, end = part.split("-")
    id_ranges.append((start, end))

ans = 0
for id_range in id_ranges:
    invalid_ids = find_invalid_ids(id_range[0], id_range[1])
    ans += sum(invalid_ids)
print(ans)
