# 5.3 Wrong Answer 0/21
n = int(input())
card = list(map(int, input().split()))

dp = [[0, 0] for i in range(n+1)]
sum = [0 for i in range(n+1)]
for i in range(1, n+1):
    sum[i] = sum[i-1] + card[i-1]

for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] + (card[i-1] / i)
    if i > 1:
        for j in range(i-1):
            dp[i][0] = max(dp[i][0], dp[j][1] + ((sum[i] - sum[j]) / (i-j)))
            dp[i][1] = max(dp[i][1], dp[j][0] + ((sum[i] - sum[j]) / (i-j)))
    dp[i][1] = max(dp[i][1], dp[i-1][0])

print("%.10f" % max(dp[n][0], dp[n][1]))
