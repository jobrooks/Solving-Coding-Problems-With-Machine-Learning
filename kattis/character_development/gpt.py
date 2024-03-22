# 2.3 wrong answer 0/8

n = int(input())
total = 0

# Use a nested loop to iterate over all pairs of characters
for i in range(1, n+1):
    for j in range(i+1, n+1):
        total += 1

# Add the final relationship for all characters together
total += n

print(total)
