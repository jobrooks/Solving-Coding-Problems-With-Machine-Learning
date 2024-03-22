# 4.3 wrong answer 1/16
n, m = map(int, input().split())
read = [-1] * n
for i in range(m):
    s = int(input()) - 1
    read[s] = i
    total_unread = 0
    for j in range(n):
        if read[j] < i:
            total_unread += 1
    print(total_unread)
