# 4.7 runtime error 0/71
def solve():
    n = int(input())
    p = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        i, j, w = map(int, input().split())
        adj[i-1].append((j-1, w))
        adj[j-1].append((i-1, w))

    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        res = p[i] ** 2
        for j, w in adj[i]:
            res = min(res, dp(j) + w*p[i]*p[j])
        memo[i] = res
        return res

    return sum(dp(i) for i in range(n))

print(solve())
