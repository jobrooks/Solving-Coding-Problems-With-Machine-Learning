# 4.9 runtime error 0/3
INF = float('inf')

while True:
    n, m, s, q = map(int, input().split())
    if n == m == s == q == 0:
        break

    # Initialize adjacency list and distances
    adj_list = [[] for _ in range(n)]
    dist = [INF] * n
    dist[s] = 0

    # Read edges
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))

    # Run Bellman-Ford algorithm
    reachable = set([s])
    for _ in range(n - 1):
        for u in range(n):
            for v, w in adj_list[u]:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    reachable.add(v)

    # Handle queries
    for _ in range(q):
        t = int(input())
        if t not in reachable:
            print('Impossible')
        elif dist[t] == INF:
            print('-Infinity')
        else:
            print(dist[t])
    print()
