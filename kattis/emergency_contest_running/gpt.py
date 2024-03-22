# 3.8 wrong answer 0/17
import heapq

def shortest_path(n, k):
    pq = [(0, 0)] # priority queue with starting node 0 and distance 0
    dist = [float('inf')] * n # initialize all distances to infinity
    dist[0] = 0 # distance from node 0 to node 0 is 0
    
    while pq:
        d, u = heapq.heappop(pq) # pop node with smallest distance
        if u == n-1: # reached the destination
            return d
        for v in [u+1] + [i for i in range(u//k*k+k, n, k) if i != u]: # generate neighbors
            if v < n: # check if neighbor is in range
                new_dist = d + 1 # distance from u to v is 1
                if new_dist < dist[v]: # update distance and add to priority queue
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
    
    return -1 # destination is not reachable

n, k = map(int, input().split())
print(shortest_path(n, k))
