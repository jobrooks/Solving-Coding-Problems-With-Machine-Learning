from bisect import bisect

with open('coffee.in', 'r') as f:
    l, a, b, t, r = [int(x) for x in f.readline().split()]
    n = int(f.readline())
    coffee_locs = [int(x) for x in f.readline().split()]

# Compute the time needed to purchase and consume coffee at a single location
purchase_duration = t + r

# Compute the time saved by purchasing coffee at each location
savings = [min(purchase_duration, (l - loc) / (b - a) * t) for loc in coffee_locs]

# Find the locations where the time saved is greater than the cost of purchasing coffee
eligible_locs = [loc for loc, time_saved in zip(coffee_locs, savings) if time_saved > purchase_duration]

# Sort the eligible locations by time saved
eligible_locs.sort(key=lambda loc: savings[coffee_locs.index(loc)])

# Purchase coffee at the locations with the highest time savings
num_purchases = 0
total_time_saved = 0
for loc in eligible_locs:
    if total_time_saved + savings[coffee_locs.index(loc)] < l / b * t:
        total_time_saved += savings[coffee_locs.index(loc)]
        num_purchases += 1
    else:
        break

# Output the number of purchases
with open('coffee.out', 'w') as f:
    f.write(str(num_purchases) + '\n')

# Output the indices of the coffee carts where purchases should be made
    locs_purchased = [coffee_locs.index(loc) for loc in eligible_locs[:num_purchases]]
    f.write(' '.join(str(loc) for loc in locs_purchased))