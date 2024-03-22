# 3.1 accepted 2/2

import math

def classify_number(n):
    divisors_sum = 1  # start with 1 since it's always a proper divisor
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    
    if divisors_sum == n:
        return "perfect"
    elif abs(divisors_sum - n) <= 2:
        return "almost perfect"
    else:
        return "not perfect"

# read input until end of file
while True:
    try:
        n = int(input())
    except:
        break
    
    classification = classify_number(n)
    print(f"{n} {classification}")
