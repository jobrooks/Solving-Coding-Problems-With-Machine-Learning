import sys

def main():
  for line in sys.stdin:
    n, m, q = map(int, line.split())
    if n == 0 and m == 0 and q == 0:
      break

    edges = []
    for _ in range(m):
      u, v, w = map(int, input().split())
      edges.append((u, v, w))

    for _ in range(q):
      u, v = map(int, input().split())
      dist, path = dijkstra(u, v, n, edges)
      if dist == float('inf'):
        print("Impossible")
      elif dist == -float('inf'):
        print("-Infinity")
      else:
        print(dist)

    print()

def dijkstra(source, destination, n, edges):
  dist = [float('inf')] * n
  dist[source] = 0
  visited = [False] * n
  visited[source] = True
  parent = [-1] * n

  while True:
    min_dist = float('inf')
    min_node = -1
    for i in range(n):
      if not visited[i] and dist[i] < min_dist:
        min_dist = dist[i]
        min_node = i

    if min_node == -1 or min_node == destination:
      break

    visited[min_node] = True
    for edge in edges:
      u, v, w = edge
      if u == min_node and not visited[v]:
        new_dist = dist[u] + w
        if new_dist < dist[v]:
          dist[v] = new_dist
          parent[v] = u
      elif v == min_node and not visited[u]:
        new_dist = dist[v] + w
        if new_dist < dist[u]:
          dist[u] = new_dist
          parent[u] = v

  if dist[destination] == float('inf'):
    return float('inf'), None
  elif dist[destination] == -float('inf'):
    return -float('inf'), None
  else:
    path = []
    curr = destination
    while curr != -1:
      path.append(curr)
      curr = parent[curr]

    path.reverse()
    return dist[destination], path

if __name__ == "__main__":
  main()