n = int(input())
a = list(map(int, input().split()))

pi = [0] * n
sigma = [0] * n

for i in range(n):
    for j in range(n):
        if pi[j] == 0 and sigma[a[i] - pi[j] - 1] == 0:
            pi[j] = a[i] - j - 1
            sigma[a[i] - pi[j] - 1] = j + 1
            break

if 0 in pi or 0 in sigma:
    print("impossible")
else:
    print(*pi)
    print(*sigma)