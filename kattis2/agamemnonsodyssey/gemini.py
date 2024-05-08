import sys
input = sys.stdin.readline
N, k = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
visited = [False] * (N + 1)
mx = 0
def dfs(node, prev, sum):
    global mx
    visited[node] = True
    mx = max(mx, sum)
    for nei, cost in graph[node]:
        if not visited[nei] and cost > 0:
            dfs(nei, node, sum + cost)
    visited[node] = False
dfs(1, 1, 0)
print(mx)