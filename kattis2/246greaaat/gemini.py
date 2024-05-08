# 8.2 Error 1/25
import sys

# Read input
N, T = map(int, input().split())
cheers = []
for i in range(N):
    S, D = map(int, input().split())
    cheers.append((S, D))

# Initialize DP table
dp = [[[0, -1] for _ in range(T+1)] for _ in range(N+1)]
dp[0][0] = [0, -1]

# Iterate over cheers
for i in range(N):
    S, D = cheers[i]
    for j in range(T+1):
        dp[i+1][j][0] = max(dp[i][j][0], dp[i+1][j][0])
        if j + S >= 0 and j + S <= T:
            if dp[i][j][0] + S == j + S and dp[i][j][1] != -1:
                dp[i+1][j+S][0] = max(dp[i+1][j+S][0], dp[i][j][0] + S)
                dp[i+1][j+S][1] = dp[i][j][1]
            if dp[i][j][0] + S == j + S:
                dp[i+1][j+S][0] = max(dp[i+1][j+S][0], dp[i][j][0] + S)
                dp[i+1][j+S][1] = i+1

# Generate output
c = dp[N][T][0]
sequence = []
i = T
while i > 0:
    j = dp[N][i][1]
    if j != -1:
        sequence.append(j)
        i -= cheers[j-1][0]
sequence.reverse()

# Output
print(c)
print(*sequence)