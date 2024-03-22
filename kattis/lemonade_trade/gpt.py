# 5.9 wrong answer 0/15
from collections import defaultdict
from queue import Queue

def convert_rate(rate):
    return int(rate * 10**7)

def bfs(adj, s, t, parent):
    q = Queue()
    visited = set()
    q.put(s)
    visited.add(s)
    parent[s] = None

    while not q.empty():
        u = q.get()
        for v, capacity in adj[u].items():
            if v not in visited and capacity > 0:
                q.put(v)
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True

    return False

def max_flow(adj, s, t):
    parent = {}
    max_flow = 0

    while bfs(adj, s, t, parent):
        path_flow = float("inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, adj[u][v])
            v = u

        v = t
        while v != s:
            u = parent[v]
            adj[u][v] -= path_flow
            adj[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

n = int(input())
adj = defaultdict(dict)

source = 'blue'
sink = 'sink'

for i in range(n):
    o, w, rate = input().split()
    rate = convert_rate(float(rate))
    adj[o][w] = rate
    adj[w][o] = 0

    adj[source][o] = 10**9
    adj[o][source] = 0

    adj[w][sink] = 10**9
    adj[sink][w] = 0

max_flow_value = max_flow(adj, source, sink)
max_blue_lemonade = min(max_flow_value, 10) # cap at 10 liters
print("{:.6f}".format(max_blue_lemonade))
