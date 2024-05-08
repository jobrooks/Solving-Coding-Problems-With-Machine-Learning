def make_palindrome(s):
    n = len(s)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n-1, -1, -1):
        for j in range(i+1, n+1):
            if s[i] == s[j-1]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

    return dp[0][n]

s = input()
print(make_palindrome(s))