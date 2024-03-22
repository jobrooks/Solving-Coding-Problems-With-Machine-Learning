# 3.9 accepted 23/23

MOD = 1000000009

N, K, T = map(int, input().split())

# Initialize DP table
dp = [[0 for _ in range(N*K+1)] for _ in range(N+1)]
for j in range(1, min(K+1, T+1)):
    dp[1][j] = 1

# Compute DP table
for i in range(2, N+1):
    for j in range(1, T+1):
        for x in range(1, min(K+1, j+1)):
            dp[i][j] += dp[i-1][j-x]
            dp[i][j] %= MOD

# Output answer
print(dp[N][T])
