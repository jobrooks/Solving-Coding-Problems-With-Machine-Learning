# 5.8 wrong answer 1/21
import math

n = int(input())

# Compute the number of factors of 5 up to the power of 3
num_fives = (n // 5) + (n // 25) + (n // 125)

# Compute the value of n! modulo 1000
fact_mod = math.factorial(n) % 1000

# Remove the last two digits and divide by 100
ans = (fact_mod // 100) % 10

if num_fives == 0:
    ans = fact_mod % 100
elif num_fives == 1:
    ans = (fact_mod // 10) % 100
elif num_fives == 2:
    ans = (fact_mod // 1) % 100

print(ans)
