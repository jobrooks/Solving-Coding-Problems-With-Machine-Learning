# 3.4 wrong answer 0/47
P = int(input())
dp = [0] * (P+1)
dp[2] = 1
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]

for i in range(3, P+1):
    for j in range(i-1, max(i-14, 1)-1, -1):
        if i-j not in primes:
            continue
        dp[i] += dp[j]
    
print(dp[P])