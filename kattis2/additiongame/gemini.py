import sys

def main():
    # Read the input
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Check if there is a solution
    if not is_valid(n, a):
        print("impossible")
        return

    # Find a solution
    pi, sigma = find_solution(n, a)

    # Print the solution
    print(' '.join(map(str, pi)))
    print(' '.join(map(str, sigma)))

def is_valid(n, a):
    # Check if the sum of any two elements is greater than n
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] > n:
                return False

    # Check if the sum of any two elements is equal to n
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == n:
                return True

    # Otherwise, there is no solution
    return False

def find_solution(n, a):
    # Create a graph of the elements in a
    graph = {}
    for i in range(n):
        graph[a[i]] = []

    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] <= n:
                graph[a[i]].append(a[j])

    # Find a cycle in the graph
    cycle = []
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, cycle):
                break

    # Create the permutations pi and sigma
    pi = [0] * n
    sigma = [0] * n
    for i in range(len(cycle)):
        pi[cycle[i]] = cycle[(i + 1) % len(cycle)]
        sigma[cycle[i]] = cycle[(i - 1) % len(cycle)]

    return pi, sigma

def dfs(node, graph, visited, cycle):
    # Mark the node as visited
    visited.add(node)

    # Add the node to the cycle
    cycle.append(node)

    # Explore the node's neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, cycle):
                return True
        elif neighbor in cycle:
            return True

    # Remove the node from the cycle
    cycle.pop()

    return False

main()