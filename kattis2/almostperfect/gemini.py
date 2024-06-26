import sys

def is_perfect(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.extend([i, n // i])
    return sum(divisors) == n

def is_almost_perfect(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.extend([i, n // i])
    return abs(sum(divisors) - n) <= 2

for line in sys.stdin:
    n = int(line)
    if is_perfect(n):
        print(n, "perfect")
    elif is_almost_perfect(n):
        print(n, "almost perfect")
    else:
        print(n, "not perfect")