# 2.0 accepted 3/3
import sys

def convert_base(num, from_base, to_base):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<>?@[\]^_`{|}~"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, 10, to_base) + alphabet[n % to_base]

def alien_to_decimal(num, base, digits):
    n = 0
    for i in range(len(num)):
        n = n * base + digits.index(num[i])
    return n

def decimal_to_alien(num, base, digits):
    res = ''
    while num > 0:
        res = digits[num % base] + res
        num = num // base
    return res

t = int(input().strip())
for i in range(1, t + 1):
    num, from_language, to_language = input().strip().split()
    from_base = len(from_language)
    to_base = len(to_language)
    n = alien_to_decimal(num, from_base, from_language)
    res = convert_base(n, 10, to_base)
    res = decimal_to_alien(n, to_base, to_language)
    print("Case #{}: {}".format(i, res))