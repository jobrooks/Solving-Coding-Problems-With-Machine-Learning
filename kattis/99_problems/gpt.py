# 2.7 wrong answer 2/19

n = int(input())

if n % 100 == 99:
    print(n)
else:
    print((n // 100 + 1) * 100 - 1)