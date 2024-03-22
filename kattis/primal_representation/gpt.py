# 4.8 accepted 2/2
import math

def prime_factorization(n):
    """Returns the prime factorization of n as a list of tuples (p, k)
    where p is a prime factor of n and k is its exponent."""
    factors = []
    if n < 0:
        factors.append((-1, 1))
        n = -n
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            k = 0
            while n % i == 0:
                k += 1
                n //= i
            factors.append((i, k))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors

# Read input integers from standard input and print their prime factorizations
import sys
for line in sys.stdin:
    x = int(line.strip())
    factors = prime_factorization(x)
    if factors[0][0] == -1:
        print("-1", end=" ")
        factors = factors[1:]
    print(" ".join([str(p) + ("" if k == 1 else "^" + str(k)) for p, k in factors]))
