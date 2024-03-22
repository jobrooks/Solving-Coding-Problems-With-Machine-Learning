# 5.3 wrong answer 0/47
import heapq

n, m = map(int, input().split())

# Build adjacency list
adj_list = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

# Initialize distances and visited array
dist = [float('inf')] * n
dist[0] = 0
visited = [False] * n

# Priority queue ordered by distance and danger level
pq = [(0, 0)]  # (distance, node)
while pq:
    d, u = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] = True
    for v in adj_list[u]:
        if dist[v] > d + 1:
            dist[v] = d + 1
            heapq.heappush(pq, (dist[v], v))
    if not pq:  # Check if there are unvisited nodes
        for i in range(n):
            if not visited[i]:
                heapq.heappush(pq, (dist[i], i))
                break

# Sum the distances and print the result
print(sum(dist))
