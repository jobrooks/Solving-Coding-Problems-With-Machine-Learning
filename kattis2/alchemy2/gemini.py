s = input()
n = len(s)
dp = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
print(dp[0][n - 1])