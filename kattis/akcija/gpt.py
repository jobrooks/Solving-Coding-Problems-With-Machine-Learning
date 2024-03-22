# 2.2 accepted 12/12

n = int(input())
prices = []

for i in range(n):
    prices.append(int(input()))

prices.sort(reverse=True)

total_cost = 0

for i in range(n):
    if i % 3 != 2:
        total_cost += prices[i]

print(total_cost)