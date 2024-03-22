# 3.9 wrong answer 0/17
import heapq

def dijkstra(adj_list, start, end):
    # Initialize distances to all nodes as infinity except for the start node
    dist = {node: float('inf') for node in adj_list}
    dist[start] = 0
    
    # Initialize the priority queue with the start node
    pq = [(0, start)]
    
    # Iterate until the priority queue is empty or we have found the shortest path to the end node
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        # If we have already found a shorter path to this node, skip it
        if curr_dist > dist[curr_node]:
            continue
            
        # Check if we have reached the end node
        if curr_node == end:
            return dist[end]
        
        # Iterate through the neighbors of the current node
        for neighbor, weight in adj_list[curr_node]:
            # Calculate the distance to the neighbor through the current node
            new_dist = curr_dist + weight
            
            # If this is a shorter path to the neighbor, update its distance and add it to the priority queue
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    # If we have not found a path to the end node, return infinity
    return float('inf')

# Read input
n, alice, rabbit, t = map(int, input().split())

# Initialize the adjacency list
adj_list = {i: [] for i in range(1, n+1)}

# Build the adjacency list from the trips
for _ in range(t):
    d, p, *a = map(int, input().split())
    for i in range(p-1):
        adj_list[a[i]].append((a[i+1], d))
        adj_list[a[i+1]].append((a[i], d))

# Find the shortest path from Alice's location to the Rabbit's hole
shortest_time = dijkstra(adj_list, alice, rabbit)

# Print the result
print(shortest_time)
