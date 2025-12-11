import sys
import pulp
from typing import List


def fewest_presses(target: List[int], switches: List[List[int]]) -> int:
    num_counters = len(target)
    num_buttons = len(switches)
    A = [[0] * num_buttons for _ in range(num_counters)]
    for j in range(num_buttons):
        for counter_index in switches[j]:
            A[counter_index][j] = 1

    prob = pulp.LpProblem("Minimum_Button_Presses", pulp.LpMinimize)

    button_vars = pulp.LpVariable.dicts(
        "Presses",
        range(num_buttons),
        lowBound=0,
        cat=pulp.LpInteger,
    )

    prob += pulp.lpSum([button_vars[j] for j in range(num_buttons)]), "Total_Presses"
    for i in range(num_counters):
        contribution_sum = pulp.lpSum(
            [A[i][j] * button_vars[j] for j in range(num_buttons)]
        )

        prob += contribution_sum == target[i], f"Counter_{i}_Requirement"

    solver = pulp.PULP_CBC_CMD(msg=False)
    prob.solve(solver)
    min_presses = pulp.value(prob.objective)
    return int(round(min_presses))


lines = sys.stdin.read().strip().split("\n")
config = []
for line in lines:
    arr = line.split(" ")[1:]
    target = arr[-1]
    target = [int(x) for x in target.strip("{}").split(",")]
    n = len(target)

    switches = []
    for v in arr[:-1]:
        switch = [int(i) for i in v.strip("()").split(",")]
        switches.append(switch)
    config.append((target, switches))

ans = 0
for target, switches in config:
    presses = fewest_presses(target, switches)
    ans += presses
print(ans)
