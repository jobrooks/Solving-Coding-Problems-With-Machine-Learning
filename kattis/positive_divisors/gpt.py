# 2.9 Accepted 53/53
import math

n = int(input())
divisors = []

# iterate from 1 to sqrt(N)
for i in range(1, int(math.sqrt(n))+1):
    # check if i divides N without remainder
    if n % i == 0:
        divisors.append(i)
        # add the complement of i if it's not equal to i
        if n // i != i:
            divisors.append(n // i)

# sort the list of divisors and print them
divisors.sort()
for d in divisors:
    print(d)
