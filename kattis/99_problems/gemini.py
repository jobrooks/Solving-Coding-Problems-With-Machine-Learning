# Difficulty: 2.8
# Justification: none
# Result: failed
# Tests passed: 0/19
# Error: none
# Response: 
def nearest_ending_99(n):
  """
  Finds the nearest positive integer to n which ends in 99.

  Args:
      n: A positive integer.

  Returns:
      The nearest positive integer to n which ends in 99.
  """

  remainder = n % 100
  if remainder <= 50:
    return n - remainder
  else:
    return n + (100 - remainder)

# Example usage
price = 783
nearest_price = nearest_ending_99(price)
print(nearest_price)
