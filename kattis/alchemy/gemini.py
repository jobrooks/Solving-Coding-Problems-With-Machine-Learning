# Difficulty: 9.1
# Justification: 
# Result: wrong answer
# Tests passed: 0/101
# Error: none
# Response: 
def min_palindrome_operations(s):
  """
  Calculates the minimum number of operations to make a string a palindrome.

  Args:
      s: A string of lowercase letters.

  Returns:
      The minimum number of operations needed.
  """
  n = len(s)
  # Create a 2D DP table to store minimum operations for substrings
  dp = [[0] * n for _ in range(n)]

  # Base cases: single characters and adjacent characters
  for i in range(n):
    dp[i][i] = 0  # Single character is already a palindrome (0 operations)
    if i < n - 1 and s[i] == s[i + 1]:
      dp[i][i + 1] = 0  # Two adjacent characters already form a palindrome (0 operations)

  # Fill the DP table bottom-up
  for length in range(3, n + 1):  # Start from length 3 (minimum for 2 changes)
    for left in range(n - length + 1):
      right = left + length - 1
      if s[left] == s[right]:
        dp[left][right] = dp[left + 1][right - 1]  # If same characters, copy from previous subproblem
      else:
        dp[left][right] = 1 + min(dp[left + 1][right], dp[left][right - 1])
        # Minimum of (change left and right characters) or (change other characters)

  # The bottom right corner of the DP table holds the minimum operations for the entire string
  return dp[0][n - 1]

# Read input string
s = input()

# Calculate and print the minimum number of operations
min_ops = min_palindrome_operations(s)
print(min_ops)
