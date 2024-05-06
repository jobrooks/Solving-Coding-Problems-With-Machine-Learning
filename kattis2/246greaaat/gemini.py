# 8.2 Error 1/25
import sys

def solve():
    n, t = map(int, input().split())
    cheers = [(int(x), int(y)) for x, y in zip(*[iter(sys.stdin.readline().split()) for _ in range(n)])]
    dp = [[(0, -1)] * (2 * t + 1) for _ in range(n + 1)]
    dp[0][t] = (0, 0)
    for i in range(n):
        s, d = cheers[i]
        for j in range(2 * t + 1):
            if dp[i][j] == (0, -1):
                continue
            k, prev = dp[i][j]
            if j + s >= 0 and j + s <= 2 * t and j + s not in (0, t):
                if dp[i+1][j+s][0] == 0 or dp[i+1][j+s][0] > k + d:
                    dp[i+1][j+s] = (k + d, prev)
            if j - s >= 0 and j - s <= 2 * t and j - s not in (0, t):
                if dp[i+1][j-s][0] == 0 or dp[i+1][j-s][0] > k + d:
                    dp[i+1][j-s] = (k + d, prev)
    k, prev = dp[n][t]
    if k == 0:
        print(-1)
        return
    ans = [prev]
    while ans[-1] != 0:
        ans.append(dp[len(cheers) - ans[-1]][t - s][1])
        s, d = cheers[len(cheers) - ans[-1] - 1]
        t -= s
    ans.reverse()
    ans.pop()
    print(len(ans))
    print(*ans)

solve()