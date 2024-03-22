# 4.3 time limit exceeded 2/15
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
    def same_set(self, x, y):
        return self.find(x) == self.find(y)
n, q = map(int, input().split())
uf = UnionFind(n)

for i in range(q):
    op, a, b = input().split()
    a, b = int(a), int(b)
    if op == "=":
        uf.union(a, b)
    else:
        print("yes" if uf.same_set(a, b) else "no")
