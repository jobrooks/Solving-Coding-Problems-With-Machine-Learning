k = int(input())
d = [int(input()) for _ in range(k)]
d.sort()
ans = d[-1] + 1
for i in range(k - 1):
    ans += d[i] + 1
print(ans)