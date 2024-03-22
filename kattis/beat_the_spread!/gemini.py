# Difficulty: 2.3
# Result: Wrong Answer
# Tests passed: 0/2
# Error: none
# Response: 
def find_final_scores(sum_score, difference):
  """
  Finds the final scores based on the sum and absolute difference.

  Args:
      sum_score: Integer representing the sum of final scores.
      difference: Integer representing the absolute difference between final scores.

  Returns:
      A tuple (larger_score, smaller_score) representing the final scores, 
      or "impossible" if no such scores exist.
  """

  # Calculate potential scores based on sum and difference
  larger_score = (sum_score + difference) // 2
  smaller_score = (sum_score - difference) // 2

  # Check if both scores are non-negative integers
  if larger_score >= 0 and smaller_score >= 0:
    return larger_score, smaller_score
  else:
    return "impossible"

# Get number of test cases
num_test_cases = int(input())

# Loop through test cases
for _ in range(num_test_cases):
  # Get sum and difference
  sum_score, difference = map(int, input().split())

  # Find final scores or determine impossibility
  final_scores = find_final_scores(sum_score, difference)

  # Print the result
  print(*final_scores)  # Use unpacking (*) to print elements of a tuple
