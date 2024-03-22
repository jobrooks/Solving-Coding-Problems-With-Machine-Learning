# Difficulty: 3.1
# Justification: 
# Result: wrong answer
# Tests passed: 0/94
# Error: none
# Response: 
def min_letters_to_make_alphabetical(s):
  """
  Calculates the minimum number of letters to add to make a string alphabetical.

  Args:
      s: A string of lowercase letters (1 <= len(s) <= 50).

  Returns:
      The minimum number of letters needed to add to s.
  """

  # Set of expected characters (lowercase letters from 'a' to 'z')
  expected_chars = set(chr(i) for i in range(ord('a'), ord('z') + 1))

  # Set of characters present in the string
  present_chars = set(s)

  # Count missing characters
  missing_chars = expected_chars - present_chars

  return len(missing_chars)

# Read input string
s = input()

# Calculate and print the minimum number of letters
min_letters = min_letters_to_make_alphabetical(s)
print(min_letters)
