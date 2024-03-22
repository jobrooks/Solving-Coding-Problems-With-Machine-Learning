# 4.3 wrong answer 1/7
MOD = 10000

def count_phrases(s):
    n = len(s)
    dp = [[0] * 19 for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, 19):
            if s[i-1] == "welcome to code jam"[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][18]

t = int(input())
for i in range(t):
    s = input().strip()
    count = count_phrases(s)
    print("Case #{}: {:04d}".format(i+1, count))
