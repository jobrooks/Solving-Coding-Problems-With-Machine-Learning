# 4.9 wrong answer 0/10
import sys

def solve(points):
    n = len(points)
    points.sort()

    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j][i] = 1

    for i in range(n):
        for j in range(i + 2, n):
            for k in range(i + 1, j):
                for l in range(i, k):
                    if points[l][1] < points[i][1] and points[l][1] < points[j][1]:
                        dp[i][j][k] += dp[i][l][k] * dp[l][j][l]
                        if l > k:
                            dp[i][j][k] -= dp[i][l][k] * dp[l][k][l]

    ans = 0
    for i in range(n):
        for j in range(i + 2, n):
            for k in range(i + 1, j):
                ans += dp[i][j][k]

    return ans

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    points = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    print(solve(points))
