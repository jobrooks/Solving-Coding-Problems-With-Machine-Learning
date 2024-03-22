# 4.8 wrong answer 0/34
h, w = map(int, input().split())

dp = [[0] * (w+1) for _ in range(h+1)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % (10**9 + 7)
        if j > 0:
            dp[1][j] = (dp[1][j] + dp[0][j-1]) % (10**9 + 7)

print(dp[h][w])
