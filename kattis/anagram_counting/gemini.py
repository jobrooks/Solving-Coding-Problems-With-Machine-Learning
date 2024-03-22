# Difficulty: 3.0
# Justification: 
# Result: passed
# Tests passed: 2/2
# Error: none
# Response: 
from collections import Counter

def count_anagrams(word):
  """
  Calculates the number of unique anagrams for a given word.

  Args:
      word: A string representing the word (containing upper and lowercase letters).

  Returns:
      An integer representing the number of unique anagrams.
  """

  # Count character occurrences with case sensitivity
  char_counts = Counter(word)

  # Formula for anagram count: factorial(total characters) / product(factorial(count of each character))
  total_chars = sum(char_counts.values())
  factorial_total = 1
  for i in range(1, total_chars + 1):
    factorial_total *= i

  product_factorials = 1
  for count in char_counts.values():
    product_factorials *= factorial(count)

  return factorial_total // product_factorials

def factorial(n):
  """
  Calculates the factorial of a non-negative integer.

  Args:
      n: A non-negative integer.

  Returns:
      The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Read input words until end of file (EOF)
while True:
  try:
    word = input()
    anagram_count = count_anagrams(word)
    print(anagram_count)
  except EOFError:
    break
