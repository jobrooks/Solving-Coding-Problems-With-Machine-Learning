import sys
input = sys.stdin.readline

n, m, k, t = map(int, input().split())

# Create a graph to store the statements
graph = [[] for _ in range(n+1)]

# Add the statements to the graph
for _ in range(m):
    a, b, s = input().split()
    a = int(a)
    b = int(b)
    graph[a].append((b, s))

# Perform a depth-first search to find all the paths from player 1 to player k
visited = [False] * (n+1)
visited[1] = True
stack = [1]
path = []

while stack:
    v = stack.pop()
    path.append(v)
    
    if v == k:
        break
    
    for u, s in graph[v]:
        if not visited[u]:
            visited[u] = True
            stack.append(u)

# Check if the path contains any imposters
imposter = False
for v in path:
    for u, s in graph[v]:
        if s == "imposter":
            imposter = True
            break

# Print the result
if imposter:
    print(-1)
else:
    print(len(path) - t - 1)