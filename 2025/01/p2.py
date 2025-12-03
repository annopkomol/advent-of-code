import sys
from typing import List, Tuple


def read_seqs() -> List[int]:
    data = sys.stdin.read().splitlines()
    parsed_data = []
    for line in data:
        if line:
            direction = line[0]
            number = int(line[1:])
            parsed_data.append((direction, number))
    return parsed_data


def rotate(rotation: Tuple[str, int], dial: int) -> Tuple[int, int]:
    direction, distance = rotation
    cnt = 0

    if direction == "R":
        d, rem = divmod(distance, 100)
        cnt += d
        if dial + rem >= 100:
            cnt += 1
    else:
        distance = -distance
        d, rem = divmod(distance, -100)
        cnt += d
        if dial != 0 and dial + rem <= 0:
            cnt += 1

    return (dial + distance) % 100, cnt


rotations = read_seqs()
dial = 50
count = 0
for rot in rotations:
    dial, cnt = rotate(rot, dial)
    count += cnt

print(count)
