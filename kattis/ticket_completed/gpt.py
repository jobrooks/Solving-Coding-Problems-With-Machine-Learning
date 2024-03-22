# 4.1 wrong answer 0/23
from collections import defaultdict

n, m = map(int, input().split())

# Build the graph
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Count the number of connected components using DFS
visited = set()
components = 0
for u in range(1, n+1):
    if u not in visited:
        components += 1
        stack = [u]
        while stack:
            v = stack.pop()
            visited.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Count the number of valid tickets
valid_tickets = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if j not in graph[i] and components == 1:
            valid_tickets += 1

# Calculate the probability
total_tickets = n*(n-1)//2
prob = valid_tickets / total_tickets

print("{:.10f}".format(prob))
