import sys
from collections import deque

def bellman_ford(n, m, edges, queries):
    # Initialize the distance array
    dist = [float('inf')] * n
    dist[0] = 0

    # Relax the edges
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return float('-inf')

    # Answer the queries
    for u, v in queries:
        if dist[v] == float('inf'):
            print("Impossible")
        else:
            print(dist[v])
    print()

def main():
    # Read the input
    test_cases = []
    for line in sys.stdin:
        n, m, q = map(int, line.split())
        if n == 0 and m == 0 and q == 0:
            break
        edges = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            edges.append((u, v, w))
        queries = []
        for _ in range(q):
            u, v = map(int, input().split())
            queries.append((u, v))
        test_cases.append((n, m, edges, queries))

    # Solve the test cases
    for n, m, edges, queries in test_cases:
        bellman_ford(n, m, edges, queries)

if __name__ == "__main__":
    main()