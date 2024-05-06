# 2.9 wrong answer 1/19
n = int(input())
x = (n // 100) * 100
if n % 100 >= 50:
    x += 99
else:
    x += (n % 100 // 10) * 100 + 99
print(x)