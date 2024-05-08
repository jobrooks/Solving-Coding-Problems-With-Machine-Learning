import sys

k = int(input())
allergens = [int(input()) for _ in range(k)]

# Find the maximum live duration among the allergens
max_duration = max(allergens)

# The number of days for the shortest conclusive non-adaptive test scheme is
# equal to the maximum live duration of the allergens
num_days = max_duration

print(num_days)