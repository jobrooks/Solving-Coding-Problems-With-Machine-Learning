import sys

for line in sys.stdin:
    n, m = map(int, line.split())
    a = list(map(int, input().split()))
    dp = [0] * n
    if a[0] == m:
        dp[0] = a[0]
    for i in range(1, n):
        dp[i] = dp[i - 1]
        if a[i] == m:
            dp[i] = max(dp[i], a[i])
        else:
            dp[i] = max(dp[i], dp[i - 1] + a[i])
    for i in range(n - 1, -1, -1):
        if a[i] == m:
            dp[i] = max(dp[i], dp[i + 1] + a[i])
        else:
            dp[i] = max(dp[i], dp[i + 1])
    print(max(dp))