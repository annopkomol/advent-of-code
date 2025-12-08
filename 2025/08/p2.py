import sys


def distance(p1, p2) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5


lines = sys.stdin.read().strip().split("\n")
ps = [(int(x), int(y), int(z)) for line in lines for x, y, z in [line.split(",")]]
n = len(ps)


class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
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

left = n - 1
for d, u, v in edges:
    if not dsu.union(u, v):
        continue
    left -= 1
    if left == 0:
        print(ps[u][0] * ps[v][0])
        break
