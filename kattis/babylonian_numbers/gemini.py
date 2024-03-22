# Difficulty: 2.2
# Result: Accepted
# Tests passed: 4/4
# Error: none
# Response: 
def convert_sexagesimal(sexagesimal_str):
  """
  Converts a sexagesimal number to decimal.

  Args:
      sexagesimal_str: A string representing the sexagesimal number (digits separated by commas).

  Returns:
      The decimal equivalent of the sexagesimal number (integer).
  """

  # Split the sexagesimal string into digits
  digits = [int(digit) if digit else 0 for digit in sexagesimal_str.split(",")]

  # Calculate decimal equivalent by multiplying each digit by its base-60 power
  decimal_value = 0
  for i, digit in enumerate(reversed(digits)):
    decimal_value += digit * (60**i)

  return decimal_value

# Get number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
  sexagesimal_str = input()
  decimal_value = convert_sexagesimal(sexagesimal_str)
  print(decimal_value)
