# 4.0 wrong answer 0/2

import math
from heapq import heappush, heappop

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def is_connected(outposts, s, d):
    n = len(outposts)
    visited = [False]*n
    heap = [(0, s)]
    while heap:
        dist, u = heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n):
            if not visited[v]:
                if euclidean_distance(*outposts[u], *outposts[v]) <= d:
                    heappush(heap, (dist+euclidean_distance(*outposts[u], *outposts[v]), v))
    return all(visited)

def minimum_D(outposts, s):
    lo, hi = 0, 14142.135
    while hi-lo > 1e-6:
        mid = (lo+hi)/2
        edges = []
        n = len(outposts)
        for i in range(n):
            for j in range(i+1, n):
                if euclidean_distance(*outposts[i], *outposts[j]) <= mid:
                    edges.append((euclidean_distance(*outposts[i], *outposts[j]), i, j))
        edges.sort()
        uf = list(range(n))
        mst_weight = 0
        for w, u, v in edges:
            if uf[u] != uf[v]:
                mst_weight += w
                pu = uf[u]
                for i in range(n):
                    if uf[i] == pu:
                        uf[i] = uf[v]
        if is_connected(outposts, s, mid):
            hi = mid
        else:
            lo = mid
    return hi

# read input
t = int(input())
for _ in range(t):
    s, p = map(int, input().split())
    outposts = [tuple(map(int, input().split())) for _ in range(p)]
    # check if all outposts have satellite channel
    if s == p:
        print("0.00")
    else:
        min_D = minimum_D(outposts, s)
        print("{:.2f}".format(min_D))
