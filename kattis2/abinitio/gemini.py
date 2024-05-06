# 7.1 Error 1/17
import sys

# Read input
v, e, q = map(int, input().split())
edges = []
for _ in range(e):
    a, b = map(int, input().split())
    edges.append((a, b))

queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # Add a new vertex
        v += 1
    elif query[0] == 2:
        # Add a new edge
        x, y = query[1:]
        edges.append((x, y))
    elif query[0] == 3:
        # Delete all edges incident to a vertex
        x = query[1]
        edges = [edge for edge in edges if edge[0] != x and edge[1] != x]
    elif query[0] == 4:
        # Remove an edge
        x, y = query[1:]
        edges = [edge for edge in edges if not (edge[0] == x and edge[1] == y)]
    elif query[0] == 5:
        # Transpose the graph
        edges = [(b, a) for a, b in edges]
    elif query[0] == 6:
        # Complement the graph
        edges = [(a, b) for a, b in edges] + [(a, b) for a, b in range(v) if a != b and (a, b) not in edges]

# Compute outdegrees and hashes
outdegrees = [0] * v
hashes = [0] * v
for a, b in edges:
    outdegrees[a] += 1
    hashes[a] = (hashes[a] * 7 + b) % (10 ** 9 + 7)

# Output the final graph
print(v)
for i in range(v):
    print(outdegrees[i], hashes[i])