# 7.1 wrong answer 1/17
import sys
from collections import defaultdict

input = sys.stdin.readline

# Read input
V, E, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
queries = [list(map(int, input().split())) for _ in range(Q)]

# Initialize graph
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)

# Initialize hashes
hashes = defaultdict(int)

# Process queries
for query in queries:
    type = query[0]

    # Add vertex
    if type == 1:
        graph[V] = []
        hashes[V] = 0
        V += 1

    # Add edge
    elif type == 2:
        u, v = query[1], query[2]
        graph[u].append(v)
        hashes[u] = hashes[u] * 7 % (10 ** 9 + 7) + v

    # Delete vertex
    elif type == 3:
        u = query[1]
        for v in graph[u]:
            hashes[v] = hashes[v] // 7 % (10 ** 9 + 7)
        del graph[u]
        del hashes[u]

    # Remove edge
    elif type == 4:
        u, v = query[1], query[2]
        graph[u].remove(v)
        hashes[u] = hashes[u] // 7 % (10 ** 9 + 7)

    # Transpose graph
    elif type == 5:
        graph_transpose = defaultdict(list)
        for u in graph:
            for v in graph[u]:
                graph_transpose[v].append(u)
        graph = graph_transpose

    # Complement graph
    elif type == 6:
        for u in graph:
            for v in range(V):
                if v not in graph[u]:
                    graph[u].append(v)

# Output result
print(V)
for u in range(V):
    print(len(graph[u]), hashes[u] % (10 ** 9 + 7))