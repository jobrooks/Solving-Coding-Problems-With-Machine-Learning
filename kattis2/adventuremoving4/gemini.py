import sys

# Read input
distance = int(input())
num_stations = int(input())
stations = []
for _ in range(num_stations):
    station = [int(x) for x in input().split()]
    stations.append(station)

# Initialize dp array
dp = [float('inf')] * (distance + 1)
dp[0] = 0

# Iterate over all distances
for i in range(1, distance + 1):
    # Iterate over all gas stations
    for station in stations:
        # If the current distance is less than the distance to the gas station, skip
        if i < station[0]:
            continue
        # If the current distance is greater than the distance to the gas station, update the dp array
        else:
            dp[i] = min(dp[i], dp[i - station[0]] + station[1])

# Output the minimum amount of money that you can spend on gas
if dp[distance] == float('inf'):
    print("Impossible")
else:
    print(dp[distance])