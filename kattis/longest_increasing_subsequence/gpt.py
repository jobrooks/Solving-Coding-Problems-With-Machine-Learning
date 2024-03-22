# 5.6 time limit exception 1/2
import sys

def longest_increasing_subsequence(a):
    n = len(a)
    dp = [1] * n
    p = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                p[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    indices = []
    while max_index != -1:
        indices.append(max_index)
        max_length -= 1
        max_index = p[max_index]
        if max_index != -1 and dp[max_index] + 1 == max_length:
            break

    return (len(indices), reversed(indices))

for line in sys.stdin:
    n = int(line)
    a = list(map(int, input().split()))
    length, indices = longest_increasing_subsequence(a)
    print(length)
    print(' '.join(str(i) for i in indices))
