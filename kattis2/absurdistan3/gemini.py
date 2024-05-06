n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

used = [False] * (n+1)
for i in range(1, n+1):
    if used[i]:
        continue
    used[i] = True
    print(i, adj[i][0])
    used[adj[i][0]] = True
    for j in adj[i][1:]:
        print(adj[i][0], j)
        used[j] = True