import sys

n, k = map(int, input().split())
times = []
 
for line in sys.stdin:
    a, b = map(int, line.split())
    times.append((a, b))

ans = 0
for i in range(n):
    l, r = times[i]
    for j in range(n):
        if i == j:
            continue

        a, b = times[j]
        if a >= l + k or b <= r:
            continue
        
        ans += 1

print(ans // 2)