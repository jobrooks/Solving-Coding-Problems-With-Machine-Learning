import sys
input = sys.stdin.readline

n, d = map(int, input().split())
frogs = []
for _ in range(n):
    l, w, h = map(int, input().split())
    frogs.append((l, w, h))

frogs.sort(key=lambda x: x[0])

dp = [0] * n

for i in range(n):
    l, w, h = frogs[i]
    if h + l > d:
        dp[i] = 1
        continue

    for j in range(i):
        if w > frogs[j][1]:
            continue
        if h + frogs[j][2] + l > d:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))