# Difficulty: 4.0
# Justification: 
# Result: wrong answer
# Tests passed: 0/2
# Error: none
# Response: 
from math import sqrt

def minimum_d(satellites, outposts, coordinates):
  """
  Calculates the minimum range D required for the transceivers in the network.

  Args:
      satellites: The number of satellite channels (integer).
      outposts: The total number of outposts (integer).
      coordinates: A list of tuples representing (x, y) coordinates of outposts (km).

  Returns:
      A float representing the minimum D value with 2 decimal places.
  """

  # Check if all outposts are connected by satellites (no radio needed)
  if satellites == outposts - 1:
    return 0.00

  # Calculate pairwise distances between outposts
  distances = []
  for i in range(outposts):
    for j in range(i + 1, outposts):
      x1, y1 = coordinates[i]
      x2, y2 = coordinates[j]
      distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
      distances.append(distance)

  # Find the maximum distance not covered by satellites (minimum required D)
  max_distance = max(distances)

  return format(max_distance, ".2f")  # Format output with 2 decimal places

# Read the number of test cases
num_cases = int(input())

for _ in range(num_cases):
  # Read input for each test case
  satellites, outposts = map(int, input().split())
  coordinates = [tuple(map(int, input().split())) for _ in range(outposts)]

  # Calculate and print the minimum D
  min_d_value = minimum_d(satellites, outposts, coordinates)
  print(min_d_value)
