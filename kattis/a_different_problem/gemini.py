# Difficulty: 2.9
# Justification: none
# Result: failed
# Tests passed: 0/3
# Error: runtime error
# Response: 
def absolute_difference(a, b):
  """
  This function calculates the absolute difference between two integers.

  Args:
      a: The first integer.
      b: The second integer.

  Returns:
      The absolute difference between a and b.
  """
  return abs(a - b)

# Read input until end of file
while True:
  try:
    a = int(input())
    b = int(input())
    difference = absolute_difference(a, b)
    print(difference)
  except EOFError:
    break
