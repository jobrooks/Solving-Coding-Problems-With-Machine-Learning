import heapq
from collections import defaultdict

def max_resources(n: int, k: int, edges: list[tuple[int, int, int]]) -> int:
    """
    Finds the maximum amount of resources Agamemnon can acquire with a feasible plan.

    Args:
    n: The number of islands of Crete.
    k: The maximum number of times a single route may be used without being discovered by Artemis.
    edges: A list of tuples representing the sea routes, where each tuple contains three integers: u, v, and c, 
        explaining that the sea route connects islands u and v and Agamemnon can acquire c units of resources
        along this route.

    Returns:
    The maximum amount of resources Agamemnon can acquire with a feasible plan.
    """

    # Create a graph to represent the islands and their connections.
    graph = defaultdict(list)
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))

    # Initialize the distances to all nodes from the starting node to infinity.
    distances = [float('inf')] * (n + 1)

    # Initialize a priority queue to store the nodes to be visited, starting with the starting node.
    pq = [(0, 1)]

    # Initialize the maximum resources to 0.
    max_resources = 0

    # While the priority queue is not empty, keep visiting nodes.
    while pq:
        # Get the node with the smallest distance from the priority queue.
        distance, node = heapq.heappop(pq)

        # If the distance to the current node is greater than the current shortest distance, skip it.
        if distance > distances[node]:
            continue

        # Update the maximum resources if necessary.
        max_resources = max(max_resources, distance)

        # Visit the node's neighbors.
        for neighbor, weight in graph[node]:
            # If the neighbor has not been visited or the new distance is shorter, update the distance to the neighbor.
            if distances[neighbor] == float('inf') or distance + weight < distances[neighbor]:
                distances[neighbor] = distance + weight
                heapq.heappush(pq, (distance + weight, neighbor))

    # Return the maximum resources.
    return max_resources