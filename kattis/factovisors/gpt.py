# 5.8 time limit exception 1/2
import math

while True:
    try:
        n, m = map(int, input().split())
        fac = math.factorial(n)
        if m <= fac and fac % m == 0:
            print(str(m) + ' divides ' + str(n) + '!')
        else:
            print(str(m) + ' does not divide ' + str(n) + '!')
    except:
        break
