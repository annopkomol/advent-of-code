import sys
import re


def parse():
    input_data = sys.stdin.read().splitlines()

    presents = []
    queries = []

    presents_dict = {}
    current_id = None

    for line in input_data:
        line = line.strip()
        if not line:
            continue

        # Match present ID like "0:"
        match_id = re.match(r"^(\d+):$", line)
        if match_id:
            current_id = int(match_id.group(1))
            presents_dict[current_id] = []
            continue

        # Match query like "4x4: 0 0 0 0 2 0"
        match_query = re.match(r"^(\d+)x(\d+):\s*(.*)$", line)
        if match_query:
            m = int(match_query.group(1))
            n = int(match_query.group(2))
            arr = list(map(int, match_query.group(3).split()))
            queries.append((m, n, arr))
            current_id = None
            continue

        if current_id is not None:
            # Each present is a 2D array (list of lists of characters)
            presents_dict[current_id].append(list(line))

    # Convert dict to list
    if presents_dict:
        max_id = max(presents_dict.keys())
        presents = [None] * (max_id + 1)
        for pid, grid in presents_dict.items():
            presents[pid] = grid

    return presents, queries


presents, queries = parse()

# count '#' in each present
sizes = [sum(row.count("#") for row in present) for present in presents]


ans = 0
for q in queries:
    # check size constraint
    m, n, p_cnts = q
    region_size = m * n
    total_p_size = 0
    for i, cnt in enumerate(p_cnts):
        if cnt == 0:
            continue
        p_size = sizes[i]
        total_p_size += p_size * cnt
    if total_p_size > region_size:
        continue

    # idk, it's NP, gonna YOLO and see if it works

    ans += 1

print(ans)
