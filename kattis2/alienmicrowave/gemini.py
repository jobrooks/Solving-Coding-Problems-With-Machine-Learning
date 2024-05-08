def is_error_prone(time, limits):
  """
  Checks if the given time is error-prone.

  Args:
    time: A string representing the cooking time.
    limits: A list of integers representing the limits for each digit in the
      cooking time.

  Returns:
    True if the given time is error-prone, False otherwise.
  """

  # Check if any of the digits exceeds the limit.
  for i in range(len(time)):
    if int(time[i]) > limits[i]:
      return False

  # Check if any of the digits can be omitted without changing the validity of
  # the cooking time.
  for i in range(len(time)):
    new_time = time[:i] + time[i + 1:]
    if len(new_time) == 0 or int(new_time) >= 1:
      return True

  # The cooking time is not error-prone.
  return False


def count_error_prone_times(limits):
  """
  Counts the number of error-prone cooking times.

  Args:
    limits: A list of integers representing the limits for each digit in the
      cooking time.

  Returns:
    The number of error-prone cooking times.
  """

  # Initialize the count to 0.
  count = 0

  # Iterate over all possible cooking times.
  for h in range(limits[0] + 1):
    for m in range(limits[1] + 1):
      for s in range(limits[2] + 1):

        # Convert the cooking time to a string.
        time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)

        # Check if the cooking time is error-prone.
        if is_error_prone(time, limits):
          # Increment the count.
          count += 1

  # Return the count.
  return count


# Get the input.
n = int(input())
limits = [int(input()) for _ in range(n)]

# Count the number of error-prone cooking times.
count = count_error_prone_times(limits)

# Print the count.
print(count)