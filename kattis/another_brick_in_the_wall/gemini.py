# Difficulty: 2.3
# Justification: 
# Result: wrong answer
# Tests passed: 0/30
# Error: none
# Response: 
def can_build_wall(h, w, bricks):
  """
  Checks if the construction worker can complete the wall with the given bricks.

  Args:
      h: The height of the wall (integer).
      w: The width of the wall (integer).
      bricks: A list of integers representing the lengths of the bricks (1 <= length <= 10).

  Returns:
      "YES" if the wall can be completed, "NO" otherwise.
  """

  # Sort bricks in descending order to prioritize filling larger gaps first
  bricks.sort(reverse=True)

  # Keep track of the remaining space in the current layer
  current_row_space = w

  # Iterate through each layer (height)
  for _ in range(h):
    # Try to fill the current layer with bricks
    for brick in bricks:
      if brick <= current_row_space:
        current_row_space -= brick
        break  # Move to the next layer if a brick fits

    # If no brick fits in the current layer, the wall cannot be completed
    if current_row_space > 0:
      return "NO"

    # Reset space for the next layer
    current_row_space = w

  # All layers were completed successfully
  return "YES"

# Read input
h, w, n = map(int, input().split())  # Read three integers on one line
bricks = list(map(int, input().split()))  # Read n integers on one line

# Check if the wall can be built and print the result
can_build = can_build_wall(h, w, bricks)
print(can_build)
