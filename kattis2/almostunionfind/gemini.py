N, M = map(int, input().split())

class DisjointSet:
    def __init__(self, n):
        self.parent = [ i for i in range(n+1) ]
        self.size = [ 1 for i in range(n+1) ]
        self.total = [ i for i in range(n+1) ]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.size[rootA] > self.size[rootB]:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]
                self.total[rootA] += self.total[rootB]
            else:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
                self.total[rootB] += self.total[rootA]

    def move(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
            self.total[rootB] += self.total[rootA]
            self.size[rootA] = 0
            self.total[rootA] = 0

    def query(self, a):
        root = self.find(a)
        return self.size[root], self.total[root]


dsu = DisjointSet(N)

for i in range(M):
    op, a, b = map(int, input().split())
    if op == 1:
        dsu.union(a, b)
    elif op == 2:
        dsu.move(a, b)
    else:
        ans = dsu.query(a)
        print(*ans)