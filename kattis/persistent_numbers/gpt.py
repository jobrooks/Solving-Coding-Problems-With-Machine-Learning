# 4.1 time limit exception 0/3
def multiply_digits(n):
    """Return the product of the digits of n."""
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10
    return product

def persistence(n):
    """Return the persistence of n."""
    count = 0
    while n >= 10:
        n = multiply_digits(n)
        count += 1
    return count

def find_smallest_number_with_persistence(p):
    """Return the smallest number with persistence p."""
    if p < 0:
        return "There is no such number"
    elif p == 0:
        return 0
    else:
        n = 1
        while persistence(n) != p:
            n += 1
        return n

# Read input and process test cases
while True:
    line = input().strip()
    if line == "-1":
        break
    n = int(line)
    print(find_smallest_number_with_persistence(n))
