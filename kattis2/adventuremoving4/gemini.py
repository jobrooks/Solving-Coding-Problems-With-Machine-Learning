from sys import stdin

# Read input
distance = int(stdin.readline())
num_stations = int(stdin.readline())
stations = []
for _ in range(num_stations):
    dist, price = map(int, stdin.readline().split())
    stations.append((dist, price))

# Initialize dp table
dp = [float('inf')] * (distance + 1)
dp[0] = 0

# Fill dp table
for i in range(1, distance + 1):
    for dist, price in stations:
        if i >= dist and dp[i - dist] != float('inf'):
            dp[i] = min(dp[i], dp[i - dist] + price)

# Output result
if dp[distance] == float('inf'):
    print("Impossible")
else:
    print(dp[distance])