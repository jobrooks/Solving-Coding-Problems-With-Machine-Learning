# Difficulty: 1.8
# Justification: 
# Result: passed
# Tests passed: 18/18
# Error: none
# Response: 
from decimal import Decimal

def char_ratios(text):
  """
  Calculates the ratios of whitespace, lowercase letters, uppercase letters, and symbols.

  Args:
      text: A string containing the preprocessed email text.

  Returns:
      A list of four decimal numbers representing the ratios.
  """

  # Initialize counters
  whitespace_count = 0
  lowercase_count = 0
  uppercase_count = 0
  symbol_count = 0

  # Count characters
  for char in text:
    if char == "_":
      whitespace_count += 1
    elif char.islower():
      lowercase_count += 1
    elif char.isupper():
      uppercase_count += 1
    else:
      symbol_count += 1

  # Calculate total characters
  total_chars = whitespace_count + lowercase_count + uppercase_count + symbol_count

  # Avoid division by zero (empty string)
  if total_chars == 0:
    return [Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0")]

  # Calculate ratios as decimals with high precision
  ratios = [
      Decimal(whitespace_count) / total_chars,
      Decimal(lowercase_count) / total_chars,
      Decimal(uppercase_count) / total_chars,
      Decimal(symbol_count) / total_chars,
  ]

  return ratios

# Read input text
text = input()

# Calculate and print ratios
ratios = char_ratios(text)
for ratio in ratios:
  print(ratio)
