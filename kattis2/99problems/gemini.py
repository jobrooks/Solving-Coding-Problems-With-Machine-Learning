# 2.9 Error 1/19
import math

n = int(input())
x = math.ceil(n/100) * 100
y = math.floor(n/100) * 100 + 99

if abs(x-n) > abs(y-n):
    print(y)
else:
    print(x)