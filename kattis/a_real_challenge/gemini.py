# Difficulty: 2.1
# Justification:
# Result: failed
# Tests passed: 0/49
# Error: none
# Response: 
import math

def fence_length(area):
  """
  Calculates the length of fence needed for a square-shaped pasture.

  Args:
      area: The area of the pasture in square meters.

  Returns:
      The total length of fence needed for the pasture, in meters.
  """

  # Calculate the side length of the square pasture.
  side_length = math.sqrt(area)

  # Since a square has 4 sides, return the perimeter (4 * side length).
  return 4 * side_length

# Example usage:
pasture_area = 10000  # Square meters
fence_length = fence_length(pasture_area)
print(f"Old MacDonald needs to buy {fence_length:.6f} meters of fence.")
