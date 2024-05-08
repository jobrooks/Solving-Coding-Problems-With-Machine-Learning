import sys
input = sys.stdin.readline

n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

frogs.sort(key=lambda x: x[2], reverse=True)  # Sort frogs by height in descending order

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n):
    l, w, h = frogs[i]
    if l > d:
        dp[i + 1] = max(dp[i + 1], dp[i] + 1)
    for j in range(i):
        if l + frogs[j][2] > d and w + frogs[j][1] <= frogs[j][1]:
            dp[i + 1] = max(dp[i + 1], dp[j] + 1)

print(max(dp))