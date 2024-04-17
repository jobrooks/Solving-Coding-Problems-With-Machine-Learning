import sys
from collections import defaultdict, deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
adj = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    q = deque([(start, a[start - 1])])
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        curr, size = q.popleft()
        for neighbor in adj[curr]:
            if not visited[neighbor] and size >= a[neighbor - 1]:
                q.append((neighbor, size + a[neighbor - 1]))
                visited[neighbor] = True
    return size

ans = []
for i in range(1, n + 1):
    ans.append(bfs(i))

print(*ans)