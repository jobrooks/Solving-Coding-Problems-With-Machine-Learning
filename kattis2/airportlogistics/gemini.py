import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def on_conveyor(x, y, x1, y1, x2, y2):
    if (x1 - x2) * (y - y1) == (y1 - y2) * (x - x1):
        if (x1 <= x <= x2) or (x2 <= x <= x1):
            return True
    return False

def get_min_time(x_a, y_a, x_b, y_b, conveyors):
    # If there are no conveyors, just walk on the floor
    if len(conveyors) == 0:
        return distance(x_a, y_a, x_b, y_b)

    # Create a graph of the conveyors
    graph = {}
    for conveyor in conveyors:
        x1, y1, x2, y2 = conveyor
        if (x1, y1) not in graph:
            graph[(x1, y1)] = []
        graph[(x1, y1)].append((x2, y2))
        if (x2, y2) not in graph:
            graph[(x2, y2)] = []
        graph[(x2, y2)].append((x1, y1))

    # Find the shortest path from A to B using Dijkstra's algorithm
    distances = {}
    for node in graph:
        distances[node] = float("inf")
    distances[(x_a, y_a)] = 0

    queue = [(0, (x_a, y_a))]
    while queue:
        current_distance, current_node = queue.pop(0)
        if current_node == (x_b, y_b):
            return current_distance
        for neighbor in graph[current_node]:
            if current_distance + 1 < distances[neighbor]:
                distances[neighbor] = current_distance + 1
                queue.append((current_distance + 1, neighbor))

    # If there is no path from A to B, return -1
    return -1

if __name__ == "__main__":
    # Parse the input
    x_a, y_a, x_b, y_b = map(float, input().split())
    n = int(input())
    conveyors = []
    for i in range(n):
        x1, y1, x2, y2 = map(float, input().split())
        conveyors.append((x1, y1, x2, y2))

    # Get the minimum time to get from A to B
    min_time = get_min_time(x_a, y_a, x_b, y_b, conveyors)

    # Print the minimum time
    print(min_time)