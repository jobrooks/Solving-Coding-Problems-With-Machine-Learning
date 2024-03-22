# 3.3 wrong answer 0/20

n = int(input())
responses = list(map(int, input().split()))

count = 0
for i in range(n):
    if responses[i] == 1:
        count += 1
    elif responses[i] > 1:
        count += responses[i] - 1

print(count)
