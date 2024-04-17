import sys
import math

mod = int(1e9) + 7

def fastpow(x: int, p: int) -> int:
    if p == 0:
        return 1

    if p == 1:
        return x

    val = fastpow(x, int(p / 2)) % mod
    val = (val * val) % mod

    if p % 2 != 0:
        return (val * x) % mod

    return val % mod

def modinv(x: int) -> int:
    return fastpow(x, mod - 2) % mod

n, q = map(int, input().split())
a = [0] * (n + 1)

for _ in range(q):
    query = list(map(int, input().split()))

    if len(query) == 3:
        t, u, v = query
        diff = v - u + 1
        prob = (diff - 1) / diff
        a[u] += 1
        a[v + 1] -= 1
    else:
        ans_num = 0
        ans_den = 1

        for i in range(1, n + 1):
            ans_num = (ans_num + a[i] ** 2) % mod
            ans_den = (ans_den * i) % mod

        print((ans_num * modinv(ans_den)) % mod)