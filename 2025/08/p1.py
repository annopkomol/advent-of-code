import math
import sys


def distance(p1, p2) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5


lines = sys.stdin.read().strip().split("\n")
ps = [(int(x), int(y), int(z)) for line in lines for x, y, z in [line.split(",")]]
n = len(ps)


# --- Disjoint Set Union (DSU) Implementation ---
class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size  # Track size of each set

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return False
        # Union by size
        if self.size[irep] < self.size[jrep]:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]
        return True

    def get_size(self, i):
        return self.size[self.find(i)]


edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((distance(ps[i], ps[j]), i, j))
edges.sort()
dsu = DSU(n)
max_edge = 1000 if n > 50 else 10

for i in range(max_edge):
    d, u, v = edges[i]
    dsu.union(u, v)

set_sizes = []
for i in range(n):
    if dsu.find(i) == i:
        set_sizes.append(dsu.get_size(i))
set_sizes.sort(reverse=True)
print(math.prod(set_sizes[:3]))
