# 4.4 wrong answer 0/3
import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] < self.rank[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1
        self.count -= 1

def count_sets(a, b, p):
    uf = UnionFind(b - a + 1)
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            if math.gcd(i, j) >= p:
                uf.union(i - a, j - a)
    return uf.count

# read input
T = int(input())
for case in range(1, T + 1):
    a, b, p = map(int, input().split())
    num_sets = count_sets(a, b, p)
    print(f"Case #{case}: {num_sets}")
