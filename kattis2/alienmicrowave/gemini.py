import math
from collections import Counter

def count_error_prone(n, limits):
  """Counts the number of error-prone cooking times in an alien microwave.

  Args:
    n: The number of time types in the alien time scheme.
    limits: A list of integers representing the number of partitions in each time type.

  Returns:
    The number of error-prone cooking times.
  """

  # Initialize a counter to store the number of each type of cooking time.
  counts = Counter()

  # Iterate over all possible cooking times.
  for i in range(10 ** n):
    # Convert the integer to a string.
    time_str = str(i)

    # Pad the string with leading zeros.
    time_str = time_str.zfill(n)

    # Check if the cooking time is valid.
    valid = True
    for j in range(n):
      if int(time_str[j]) >= limits[j]:
        valid = False
        break

    # If the cooking time is valid, increment the counter.
    if valid:
      counts[time_str] += 1

  # Initialize a set to store the error-prone cooking times.
  error_prone = set()

  # Iterate over the counter.
  for time_str, count in counts.items():
    # If the count is greater than 1, then the cooking time is error-prone.
    if count > 1:
      error_prone.add(time_str)

  # Return the number of error-prone cooking times.
  return len(error_prone)


if __name__ == "__main__":
  # Read the input.
  n = int(input())
  limits = [int(x) for x in input().split()]

  # Count the number of error-prone cooking times.
  error_prone = count_error_prone(n, limits)

  # Print the number of error-prone cooking times.
  print(error_prone)