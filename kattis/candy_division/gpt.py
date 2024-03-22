# 4.0 wrong answer 0/11
n = int(input())
friends = []

# iterate through all possible factors of n
for i in range(1, int(n**0.5)+1):
    # check if i is a factor of n
    if n % i == 0:
        # check if n divided by i results in an integer
        if (n // i) != i and (n // i) % i == 0:
            friends.append(i)
            friends.append(n // i)

# sort the list of friends and output them
friends.sort()
print(*friends)
