import sys

s = input()

n = len(s)
num_space = s.count("_")
num_lower = sum(c.islower() for c in s)
num_upper = sum(c.isupper() for c in s)
num_symbol = n - num_space - num_lower - num_upper

print(num_space / n)
print(num_lower / n)
print(num_upper / n)
print(num_symbol / n)