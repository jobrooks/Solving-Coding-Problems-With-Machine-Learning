# 2.7 accepted 3/3
def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % (10 ** 9 + 7)
    return dp[n]

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(solve(n))