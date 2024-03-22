# 1.9 accepted 32/32

# Read the input from the user
s = input()

# Calculate the sum of ASCII codes and the number of characters in s
sum_ascii = sum(ord(c) for c in s)
n_chars = len(s)

# Calculate the average ASCII code and round down to the nearest integer
avg_ascii = int(sum_ascii / n_chars)

# Output the character with the calculated ASCII code
print(chr(avg_ascii))