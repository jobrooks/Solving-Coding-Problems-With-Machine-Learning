# Difficulty: 1.2-2.7
# Justification: 
# Result: Accepted
# Tests passed: 35/54
# Error: none
# Response: 
from collections import Counter

def min_max_occurrence(n, k, arr):
  """
  Calculates the minimum maximum occurrence after removing K elements from the array.

  Args:
      n: The size of the array (integer).
      k: The number of elements to remove (integer).
      arr: The array of integers.

  Returns:
      The minimum possible maximum occurrence after removing K elements.
  """

  # Count element occurrences
  element_counts = Counter(arr)

  # Sort occurrences in descending order (most frequent first)
  sorted_counts = sorted(element_counts.items(), key=lambda x: x[1], reverse=True)

  # Initialize maximum occurrence and elements to remove
  max_occurrence = sorted_counts[0][1]  # Maximum occurrence (frequency of first element)
  elements_to_remove = k

  # Remove elements from the most frequent ones
  for count in sorted_counts:
    element, frequency = count
    # Limit removal to available elements and remaining K
    remove_count = min(frequency, elements_to_remove)
    elements_to_remove -= remove_count

    # Update maximum occurrence if necessary
    max_occurrence = min(max_occurrence, frequency - remove_count)

    # If all K elements are removed, stop iterating
    if elements_to_remove == 0:
      break

  return max_occurrence

# Read input (faster I/O with list comprehension)
n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

# Calculate and print the minimum maximum occurrence
min_max_occurrence_value = min_max_occurrence(n, k, arr)
print(min_max_occurrence_value)
