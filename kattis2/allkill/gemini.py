from collections import Counter
from functools import reduce

def pohlig_hellman(a, b, p):
    # Find the prime factors of p - 1 and their exponents
    factors = []
    for i in range(2, int(p**0.5) + 1):
        if (p - 1) % i == 0:
            exp = 0
            while (p - 1) % i == 0:
                (p - 1) //= i
                exp += 1
            factors.append((i, exp))
    if p - 1 > 1:
        factors.append((p - 1, 1))

    # Create a table of powers of a for each prime factor
    powers = {}
    for p, e in factors:
        powers[p] = [pow(a, i, p) for i in range(e)]

    # Solve the Chinese Remainder Theorem for each prime factor
    x = 0
    for p, e in factors:
        # Solve x = b mod p^e
        y = pow(a, p - 2, p)
        x += (b % (p**e)) * y * powers[p][-1] % (p**e)
        x %= p**e

    return x

def main():
    # Read input
    n, t = map(int, input().split())
    times = [int(input()) for _ in range(n)]

    # Preprocess times
    freq = Counter(times)
    unique_times = list(freq.keys())
    unique_times.sort()
    num_unique_times = len(unique_times)

    # Compute the probability that the last problem is finished coding by the end of the contest
    p = 1
    for time in unique_times:
        p *= (1 - time / t)**freq[time]

    # Compute the probability that all problems are finished coding by the end of the contest
    p *= 1 - (1 - 1 / t)**n

    # Compute (p * t^n) mod modulo
    modulo = 998244353
    result = pow(t, n, modulo) * p % modulo

    # Output the result
    print(result)

if __name__ == "__main__":
    main()