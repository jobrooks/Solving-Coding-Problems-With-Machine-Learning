# 2.7 wrong answer 0/54

from collections import Counter

# Function to check if it's possible to get a maximum occurrence <= limit
def is_possible(limit, k, counter):
    # Sort the counts in non-decreasing order
    counts = sorted(counter.values())
    # Calculate the number of elements to remove
    removed = sum(counts[:len(counts) // 2])
    return removed <= k

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Count the occurrences of each element in the array
counter = Counter(a)

# Binary search for the minimum possible maximum occurrence
left = 1
right = n
while left < right:
    mid = (left + right) // 2
    if is_possible(mid, k, counter):
        right = mid
    else:
        left = mid + 1

# Print the result
print(left)
