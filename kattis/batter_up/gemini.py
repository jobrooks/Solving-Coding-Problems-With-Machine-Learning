# Difficulty: 1.5
# Result: Accepted
# Tests passed: 20/20
# Error: none
# Response: 
def calculate_slugging_percentage(at_bats):
  """
  Calculates the slugging percentage of a player based on at-bats.

  Args:
      at_bats: A list of integers representing bases earned in each at-bat (0, 1, 2, 3, 4, or -1 for walk).

  Returns:
      A float representing the slugging percentage, accurate to 10^-3.
  """

  # Count valid at-bats (excluding walks)
  valid_at_bats = len([ab for ab in at_bats if ab != -1])

  if valid_at_bats == 0:
    # No valid at-bats, return 0.0 for slugging percentage
    return 0.0

  # Calculate total bases earned
  total_bases = sum(bases for bases in at_bats if bases != -1)

  # Calculate slugging percentage (total bases / valid at-bats)
  return total_bases / valid_at_bats

# Get number of at-bats
num_at_bats = int(input())

# Get list of bases earned in each at-bat
at_bats = list(map(int, input().split()))

# Calculate and print slugging percentage with high precision
slugging_percentage = calculate_slugging_percentage(at_bats)
print(f"{slugging_percentage:.3f}")
