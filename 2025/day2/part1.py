import os
import sys
from typing import List


def find_invalid_ids(first: str, last: str) -> List[int]:
    if len(first) % 2 != 0:
        first = "1" + "0" * len(first)
    if len(last) % 2 != 0:
        last = "9" * (len(last) - 1)
    if int(first) > int(last):
        return []
    halflen = len(first) // 2
    common = os.path.commonprefix([first, last])

    # common > halflen
    if len(common) >= halflen:
        invalid = common[:halflen] * 2
        if first <= invalid <= last:
            return [int(invalid)]
        else:
            return []

    first_brute = first[len(common) : halflen]
    last_brute = last[len(common) : halflen]
    ans = []
    for i in range(int(first_brute), int(last_brute) + 1):
        invalid = common + str(i).zfill(halflen - len(common))
        invalid += invalid
        if first <= invalid <= last:
            ans.append(int(invalid))

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
