# Difficulty: 2.5
# Justification: 
# Result: wrong answer
# Tests passed: 0/12
# Error: none
# Response: 
def max_discount(prices):
  """
  Calculates the maximum possible discount a customer can get.

  Args:
      prices: A list of integers representing book prices.

  Returns:
      The maximum discount the customer can get.
  """
  # Sort the prices in ascending order
  prices.sort()

  # Initialize variables
  n = len(prices)
  max_discount = 0

  # Iterate through possible values of M (number of cheapest books)
  for m in range(1, n + 1):
    # Check if N is divisible by M
    if n % m == 0:
      # Calculate the discount for this value of M
      discount = sum(prices[:m])
      # Update max_discount if this discount is larger
      max_discount = max(max_discount, discount)

  return max_discount

# Read input
n = int(input())
prices = [int(x) for x in input().split()]

# Calculate and print the maximum discount
max_discount_value = max_discount(prices)
print(max_discount_value)
