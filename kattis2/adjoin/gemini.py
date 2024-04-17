from collections import defaultdict
import sys

# Read input
n, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

# Create a graph
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# Perform a depth-first search to find the maximum number of hops
max_hops = 0
visited = [False] * n
for i in range(n):
    if not visited[i]:
        max_hops = max(max_hops, dfs(graph, i, -1, 0))

# Print the maximum number of hops
print(max_hops)

# Depth-first search function
def dfs(graph, node, parent, depth):
    visited[node] = True
    max_depth = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            max_depth = max(max_depth, dfs(graph, neighbor, node, depth + 1))
    return max_depth