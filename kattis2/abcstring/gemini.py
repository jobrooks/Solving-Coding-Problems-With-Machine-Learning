# 5.2 wrong answer 1/9
def min_beautiful_subsequences(s):
  """
  Finds the minimum number of subsequences that a given string can be partitioned into such that each subsequence is a beautiful string.

  Args:
    s (str): The string to partition.

  Returns:
    int: The minimum number of beautiful subsequences.
  """

  # Count the number of occurrences of each character in the string.
  char_counts = {}
  for char in s:
    if char not in char_counts:
      char_counts[char] = 0
    char_counts[char] += 1

  # Check all possible character combinations, and return the minimum number of subsequences required to cover all characters.
  min_subsequences = -1
  for char in char_counts:
    # Check if the current character's count is enough to form subsequences with one character of each type.
    if char_counts[char] >= 3:
      subsequences = char_counts[char] // 3
      if min_subsequences == -1 or subsequences < min_subsequences:
        min_subsequences = subsequences

  return min_subsequences