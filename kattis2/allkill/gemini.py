import functools

mod = 998244353

def fast_pow(x, p):
    if p == 0:
        return 1
    if p == 1:
        return x

    val = fast_pow(x, int(p / 2))
    val = (val * val) % mod
    if p % 2 != 0:
        val = (val * x) % mod

    return val % mod

def get_denominator(n):
    den = 1
    for i in range(1, n + 1):
        den = (den * i) % mod
    
    return den

n, t = map(int, input().split())
times = [int(x) for x in input().split()]
times.sort()

num = 1
for time in times:
    num = (num * fast_pow(time, t)) % mod

den = get_denominator(n)
result = (num * fast_pow(den, mod - 2)) % mod
print(result)