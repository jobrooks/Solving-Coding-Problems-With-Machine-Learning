# 4.7 runtime error 1/2
import math

def stirling(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

while True:
    n = int(input())
    if n == 0:
        break
    fac = math.factorial(n)
    s = stirling(n)
    print("{:.10f}".format(fac / s))
