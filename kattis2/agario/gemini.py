import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
adj = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Perform BFS from each player as starting point and calculate the maximum size
max_size = [0] * (n + 1)
for start in range(1, n + 1):
    q = deque([(start, a[start - 1])])
    visited = set([start])
    while q:
        u, size = q.popleft()
        max_size[start] = max(max_size[start], size)
        for v in adj[u]:
            if v not in visited and size >= a[v - 1]:
                visited.add(v)
                q.append((v, size + a[v - 1]))

# Print the maximum possible final size for each player
print(*max_size[1:])