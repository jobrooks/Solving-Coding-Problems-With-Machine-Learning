# 4.8 memory limit exceeded 1/2
import math

n, q = map(int, input().split())

# sieve of Eratosthenes
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(n))+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

# count the number of primes less than or equal to n
num_primes = sum(is_prime)

print(num_primes)

# answer the queries
for i in range(q):
    x = int(input())
    if is_prime[x]:
        print(1)
    else:
        print(0)
