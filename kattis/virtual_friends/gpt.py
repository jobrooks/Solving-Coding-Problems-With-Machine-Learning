# 4.5 accepted 4/4
from collections import defaultdict

def find(network, x):
    """Find the root of the network that x belongs to."""
    if network[x] == x:
        return x
    root = find(network, network[x])
    network[x] = root  # path compression
    return root

def merge(network, size, x, y):
    """Merge the network that x belongs to with the network that y belongs to."""
    x_root = find(network, x)
    y_root = find(network, y)
    if x_root != y_root:
        network[x_root] = y_root
        size[y_root] += size[x_root]
    return size[y_root]

# read input
t = int(input())
for _ in range(t):
    f = int(input())
    network = defaultdict(str)
    size = defaultdict(int)
    for _ in range(f):
        x, y = input().split()
        if not network[x]:
            network[x] = x
            size[x] = 1
        if not network[y]:
            network[y] = y
            size[y] = 1
        print(merge(network, size, x, y))
