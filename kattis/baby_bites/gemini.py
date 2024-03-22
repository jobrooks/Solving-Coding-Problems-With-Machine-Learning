# Difficulty: 1.9
# Result: wrong answer
# Tests passed: 0/33
# Error: none
# Response: 
def is_valid_counting(bites):
  """
  Checks if Arild's counting of bites makes sense.

  Args:
      bites: A list of words spoken by Arild for each bite (strings).

  Returns:
      "makes sense" if counting is valid, "something is fishy" otherwise.
  """

  # Initialize expected count and previous count
  expected_count = 1
  prev_count = None

  # Iterate through words spoken for each bite
  for word in bites:
    # Check for mumble
    if word == "mumble":
      continue

    # Convert word to integer
    try:
      count = int(word)
    except ValueError:
      return "something is fishy"  # Non-integer encountered

    # Check for valid counting sequence
    if count < expected_count:
      return "something is fishy"  # Counted backwards
    elif count != expected_count and (prev_count is None or count != prev_count + 1):
      return "something is fishy"  # Jumped in counting or repeated a number
    
    # Update expected count and previous count
    expected_count = count
    prev_count = count

  # Counting makes sense if loop completes without issues
  return "makes sense"

# Read number of bites
n = int(input())

# Read words spoken by Arild
bites = input().strip().split()

# Check if counting makes sense and print result
result = is_valid_counting(bites)
print(result)
