# Difficulty: 1.7
# Justification: 
# Result: Accepted
# Tests passed: 28/28
# Error: none
# Response: 
def smallest_square(center_x, center_y, radius):
  """
  Calculates the coordinates of the smallest square enclosing a circle.

  Args:
      center_x: The x-coordinate of the circle's center (integer).
      center_y: The y-coordinate of the circle's center (integer).
      radius: The radius of the circle (integer).

  Returns:
      A list of four tuples, each representing the (x, y) coordinates of a corner of the square.
  """

  # Calculate coordinates of top-left corner
  top_left_x = center_x - radius
  top_left_y = center_y + radius

  # Generate corner coordinates in clockwise order
  corners = [
      (top_left_x, top_left_y),  # Top left
      (top_left_x, top_left_y - 2 * radius),  # Bottom left
      (top_left_x + 2 * radius, top_left_y - 2 * radius),  # Bottom right
      (top_left_x + 2 * radius, top_left_y),  # Top right
  ]

  return corners

# Read input
center_x, center_y = map(int, input().split())
radius = int(input())

# Calculate and print corner coordinates
corners = smallest_square(center_x, center_y, radius)
for corner in corners:
  print(*corner)  # Print each corner coordinate on a separate line
