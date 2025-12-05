import sys


def parse_input():
    input_data = sys.stdin.read().strip()
    parts = input_data.split("\n\n")

    ranges_raw = parts[0].splitlines()
    ranges = []
    for line in ranges_raw:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    numbers_raw = parts[1].splitlines()
    numbers = [int(line) for line in numbers_raw]
    numbers.sort()

    return ranges, numbers


def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged


ranges, numbers = parse_input()
ranges = merge_intervals(ranges)
ans = 0
i = 0
for v in numbers:
    s, e = ranges[i]
    while i < len(ranges) - 1 and v > e:
        i += 1
        s, e = ranges[i]

    if s <= v <= e:
        ans += 1

print(ans)
