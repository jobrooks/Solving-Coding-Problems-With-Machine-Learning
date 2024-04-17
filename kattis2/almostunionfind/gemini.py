import sys

# Create a quick union find data structure
class QuickUnionFind:
    def __init__(self, n):
        self.__parent = list(range(n))
        self.__count = [1] * n
        self.__sum = list(range(n))

    def find(self, p):
        # find the root of the tree containing p
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p

    def union(self, p, q):
        # unite the trees containing p and q
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        # make the root of the smaller tree a child of the root of the larger tree
        if self.__count[p_root] < self.__count[q_root]:
            self.__parent[p_root] = q_root
            self.__count[q_root] += self.__count[p_root]
            self.__sum[q_root] += self.__sum[p_root]
        else:
            self.__parent[q_root] = p_root
            self.__count[p_root] += self.__count[q_root]
            self.__sum[p_root] += self.__sum[q_root]

    def move(self, p, q):
        # move p to the tree containing q
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        # remove p from its current tree
        self.__count[p_root] -= 1
        self.__sum[p_root] -= p

        # add p to the tree containing q
        self.__parent[p] = q_root
        self.__count[q_root] += 1
        self.__sum[q_root] += p

    def count(self, p):
        # return the number of elements in the tree containing p
        return self.__count[self.find(p)]

    def sum(self, p):
        # return the sum of elements in the tree containing p
        return self.__sum[self.find(p)]

# Read the input
n, m = map(int, sys.stdin.readline().split())
uf = QuickUnionFind(n)
for _ in range(m):
    op, p, q = map(int, sys.stdin.readline().split())
    if op == 1:
        uf.union(p - 1, q - 1)
    elif op == 2:
        uf.move(p - 1, q - 1)
    elif op == 3:
        print(uf.count(p - 1), uf.sum(p - 1))