# 5.4 Wrong Answer 13/21
import sys

# Read input values
profit, profit_pita, profit_pizza = map(float, input().split())

# Initialize list of solutions
solutions = []

# Check all possible combinations of pitas and pizzas sold
for pitas in range(int(profit/profit_pita)+1):
    for pizzas in range(int(profit/profit_pizza)+1):
        # If the combination yields the expected profit, add it to the list of solutions
        if abs(pitas * profit_pita + pizzas * profit_pizza - profit) < 0.001:
            solutions.append((pitas, pizzas))

# If no solutions were found, print "none" and exit
if not solutions:
    print("none")
    sys.exit()

# Sort the list of solutions by the number of pitas sold
solutions.sort(key=lambda x: x[0])

# Print each solution in the sorted list
for solution in solutions:
    print(solution[0], solution[1])
