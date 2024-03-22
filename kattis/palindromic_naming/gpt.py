P# 5.3 wrong answer 0/5
MOD = 1000000007

def count_palindromic_subsequences(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + dp[i][j-1] + dp[i+1][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
            dp[i][j] %= MOD
    return dp[0][n-1]

t = int(input())
for _ in range(t):
    s = input().strip()
    print(count_palindromic_subsequences(s))
