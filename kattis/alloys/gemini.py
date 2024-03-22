# Difficulty: 4.1
# Justification: 
# Result: wrong answer
# Tests passed: 0/7
# Error: none
# Response: 
from decimal import Decimal

def max_hardness(price_per_kg):
  """
  Calculates the maximum hardness of the drill alloy for a given price per kg.

  Args:
      price_per_kg: The price of the alloy per kilogram (decimal number).

  Returns:
      The maximum achievable hardness (decimal number).
  """
  price = Decimal(str(price_per_kg))

  # Constraint: x + y + z = 1
  # Maximize hardness: xy
  # We can use AM-GM inequality: (a + b + c)/3 >= sqrt(abc)

  # Substitute a = x(price), b = y(price), c = z(price)
  # (price * (x + y + z)) / 3 >= sqrt(x(price) * y(price) * z(price))
  # price >= 3 * sqrt(xyz * price^3)
  # Divide both sides by price^3 (non-zero price):
  # 1 / price^3 >= 3 * sqrt(xyz)
  # Cube both sides:
  # 1 / price^6 >= 27 * xyz
  # Maximize xyz by making x, y, z as close to each other as possible:
  # Set x = y = z = (1 - price) / 3

  max_xyz = ((1 - price) / 3) ** 3

  # Maximum hardness: xy = ((1 - price) / 3) ^ 2
  max_hardness = ((1 - price) / 3) ** 2

  return max_hardness

# Example usage (replace with actual input)
price_per_kg = 1.234567
max_hardness_value = max_hardness(price_per_kg)
print(max_hardness_value)
