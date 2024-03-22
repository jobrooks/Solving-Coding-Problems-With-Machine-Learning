# 5.6 Time Limit Exception 4/15

MOD = 10**9 + 7

n, c = map(int, input().split())

dp = [[0 for j in range(c+1)] for i in range(n+1)]
dp[1][0] = 1

for i in range(2, n+1):
    for j in range(c+1):
        for k in range(max(0, j-i+1), j+1):
            dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

print(dp[n][c])
