import sys


lines = sys.stdin.read().strip().split("\n")
adj = {}
for line in lines:
    f, too_str = line.split(":")
    f = f.strip()
    t = too_str.strip().split(" ")
    adj[f] = t

cache = {}


def dfs(f: str):
    if f in cache:
        return cache[f]
    if f == "out":
        return 1
    total = 0
    for t in adj[f]:
        total += dfs(t)
    cache[f] = total
    return total


print(dfs("you"))
