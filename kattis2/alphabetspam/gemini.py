import sys

line = input()
line = line.replace(" ", "_")
n = len(line)

count_whitespace = 0
count_lowercase = 0
count_uppercase = 0
count_symbols = 0

for c in line:
    if c == "_":
        count_whitespace += 1
    elif c.islower():
        count_lowercase += 1
    elif c.isupper():
        count_uppercase += 1
    else:
        count_symbols += 1

ratio_whitespace = count_whitespace / n
ratio_lowercase = count_lowercase / n
ratio_uppercase = count_uppercase / n
ratio_symbols = count_symbols / n

print(f"{ratio_whitespace:.12f}")
print(f"{ratio_lowercase:.12f}")
print(f"{ratio_uppercase:.12f}")
print(f"{ratio_symbols:.12f}")