# 2.8 Runtime Error 0/5
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
t = int(input())

for i in range(t):
# read the number of islands and their positions
    m = int(input())
    islands = []
    for j in range(m):
        x, y = map(float, input().split())
        islands.append((x, y))
# initialize the minimum spanning tree with the first island
mst = [0]
total_cost = 0

while len(mst) < m:
    # find the closest island to the current MST
    closest_island = None
    closest_distance = float('inf')
    for j in range(m):
        if j not in mst:
            for k in mst:
                d = distance(islands[j], islands[k])
                if d < closest_distance:
                    closest_island = j
                    closest_distance = d
    
    # add the closest island to the MST and update the cost
    mst.append(closest_island)
    total_cost += closest_distance

print("{:.3f}".format(total_cost)) # format the output with 3 decimal places
