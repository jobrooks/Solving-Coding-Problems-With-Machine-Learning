from collections import defaultdict, deque
from heapq import heappush, heappop

# Read the input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Initialize the graph
graph = defaultdict(list)
for i in range(n):
    for j in range(n):
        if i != j and flight_times[i][j] > 0:
            graph[i].append((j, flight_times[i][j]))

# Initialize the distances
distances = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    distances[i][i] = 0

# Initialize the priority queue
pq = [(0, 0)]

# Perform Dijkstra's algorithm
while pq:
    d, u = heappop(pq)
    if d > distances[u][0]:
        continue
    for v, w in graph[u]:
        if d + w < distances[v][0]:
            distances[v][0] = d + w
            distances[v][1] = u
            heappush(pq, (d + w, v))

# Initialize the number of planes needed
num_planes = 0

# Process the flights
for s, f, t in flights:
    # Find the shortest path from the source to the destination
    path = []
    u = f
    while u != s:
        path.append(u)
        u = distances[u][1]
    path.append(s)

    # Check if we need to add a new plane
    if len(path) > num_planes:
        num_planes += 1

    # Update the earliest arrival time at the destination
    earliest_arrival_time = t
    for u in path:
        earliest_arrival_time -= inspection_times[u]
        earliest_arrival_time = max(earliest_arrival_time, distances[u][0])

    # Update the distances at the destination
    for v in graph[f]:
        distances[v][0] = max(distances[v][0], earliest_arrival_time + flight_times[f][v])

# Output the minimum number of planes needed
print(num_planes)