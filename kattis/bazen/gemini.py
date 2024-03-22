# Difficulty: 2.5
# Result: Wrong Answer
# Tests passed: 0/13
# Error: none
# Response: 
def find_other_endpoint(endpoint):
  """
  Finds the other endpoint of the line segment dividing the pool equally.

  Args:
      endpoint: A tuple (x, y) representing coordinates of one endpoint.

  Returns:
      A tuple (x, y) representing coordinates of the other endpoint.
  """

  x, y = endpoint
  # Hypotenuse of the isosceles right triangle (legs are 250)
  hypotenuse = 250 * 2**0.5

  # Since the pool is divided into two parts of equal area,
  # the other endpoint will be at a distance of hypotenuse/2 from the first endpoint
  # on the opposite leg of the triangle.

  if x == 0:  # Endpoint on y-axis (left or right edge)
    other_x = hypotenuse / 2
    other_y = y
  else:  # Endpoint on x-axis (top edge)
    other_x = x
    other_y = hypotenuse / 2 - abs(y)

  return round(other_x, 2), round(other_y, 2)

# Get coordinates of one endpoint
x, y = map(int, input().split())

# Find and print coordinates of the other endpoint
other_x, other_y = find_other_endpoint((x, y))
print(f"{other_x:.2f} {other_y:.2f}")
