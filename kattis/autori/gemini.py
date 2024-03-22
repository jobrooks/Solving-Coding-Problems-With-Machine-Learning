# Difficulty: 1.2
# Justification: 
# Result: wrong answer
# Tests passed: 0/13
# Error: none
# Response:
def long_to_short(name):
  """
  Converts a long variation of a scientific discovery name to short variation.

  Args:
      name: The name string with full last names and hyphens (string).

  Returns:
      The short variation of the name with first letters capitalized (string).
  """

  # Initialize short name with the first letter capitalized
  short_name = name[0].upper()

  # Iterate through the name, extracting first letters after hyphens
  for char in name[1:]:
    if char == '-':
      short_name += char  # Include hyphen for multi-word names
      short_name += next(c for c in name[name.index(char) + 1:] if c.isupper())

  return short_name

# Read input
name = input()

# Convert and print the short variation
short_variation = long_to_short(name)
print(short_variation)
