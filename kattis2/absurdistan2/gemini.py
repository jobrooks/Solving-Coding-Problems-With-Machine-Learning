from decimal import Decimal, getcontext

getcontext().prec = 102

def fact(n):
    return Decimal(1) if n == 0 else n * fact(n - 1)

def binomial(n, k):
    return fact(n) / (fact(k) * fact(n - k))

def prob_connected(n):
    return Decimal(1.000000000000) - Decimal(2.0) / binomial(n, (n - 1) // 2)

n = int(input())

print(prob_connected(n))