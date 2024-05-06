import sys

def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    # Perform DFS to find connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, edges, visited, component)
            components.append(component)

    # Check if it is possible to satisfy the requirements
    possible = True
    for component in components:
        if len(component) == 1:
            continue
        lounges = [0] * len(component)
        for i in range(len(component)):
            for j in range(i + 1, len(component)):
                a, b = component[i], component[j]
                for edge in edges[a]:
                    if edge[0] == b:
                        lounges[i] += edge[1]
                        lounges[j] += edge[1]
                        break
        if max(lounges) > 1:
            possible = False
            break

    # Output the minimum number of lounges necessary
    if possible:
        print(max(lounges))
    else:
        print("impossible")

def dfs(node, edges, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor, _ in edges[node]:
        if not visited[neighbor]:
            dfs(neighbor, edges, visited, component)

if __name__ == "__main__":
    main()