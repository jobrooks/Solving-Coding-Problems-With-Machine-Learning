import sys
from math import sqrt

def solve(n, ap):
    # Sort the access points by their x-coordinates
    ap.sort(key=lambda x: x[0])

    # Initialize the minimum cost to connect each team to its access point
    min_cost = [0] * n

    # Iterate over the teams in order of their x-coordinates
    for i in range(n):
        # Find the access point with the closest x-coordinate
        j = bisect.bisect_left(ap, (min_cost[i], -sys.maxsize))

        # Calculate the cost of connecting the team to the access point
        cost = (min_cost[i] - ap[j][0]) ** 2 + (ap[j][1] - i) ** 2

        # Update the minimum cost to connect the team to its access point
        min_cost[i] = cost

    # Return the minimum total cost of all UTP cables required to connect the teams to their access points
    return min_cost[-1]

# Get the number of teams
n = int(input())

# Get the locations of the access points
ap = []
for i in range(n):
    s, t = map(int, input().split())
    ap.append((s, t))

# Solve the problem
result = solve(n, ap)

# Print the result
print(result)