import sys


lines = sys.stdin.read().strip().split("\n")
adj = {}
for line in lines:
    f, too_str = line.split(":")
    f = f.strip()
    t = too_str.strip().split(" ")
    adj[f] = t

cache = {}


def dfs(f: str, fft: bool, dac: bool):
    if (f, fft, dac) in cache:
        return cache[(f, fft, dac)]
    if f == "fft":
        fft = True
    if f == "dac":
        dac = True
    if f == "out":
        return fft and dac
    total = 0
    for t in adj[f]:
        total += dfs(t, fft, dac)
    cache[(f, fft, dac)] = total
    return total


print(dfs("svr", False, False))
