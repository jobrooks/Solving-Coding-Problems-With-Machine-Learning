# 3.1 accepted 23/23
def is_palindrome(n, base):
    """Check if a number is palindromic in the given base."""
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return digits == digits[::-1]

def palindromic_numbers(a, b, k):
    """Count the numbers palindromic in every base from 2 to k."""
    count = 0
    for n in range(a, b+1):
        if all(is_palindrome(n, base) for base in range(2, k+1)):
            count += 1
    return count

a, b, k = map(int, input().split())
print(palindromic_numbers(a, b, k))
