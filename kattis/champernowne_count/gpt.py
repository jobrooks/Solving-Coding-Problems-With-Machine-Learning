# 3.0 Time Limit Exception 3/101

n, k = map(int, input().split())

count = 0
for i in range(1, n+1):
    word = ''.join(str(j) for j in range(1, i+1))
    if int(word) % k == 0:
        count += 1

print(count)
