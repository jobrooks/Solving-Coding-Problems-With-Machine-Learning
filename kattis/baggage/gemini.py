# Difficulty: 5.2 
# Result: Run-time error
# Tests passed: 0/40
# Error: run-time
# Response: 
def sort_baggage_bins(n):
  """
  Finds a shortest sequence of moves to reorder baggage bins.

  Args:
      n: Number of counters (integer).

  Returns:
      A list of moves as strings ("from f to t").
  """

  # Initialize empty lists for movable pairs
  movable_a = []
  movable_b = []

  # Identify movable pairs
  for i in range(1, 2*n):
    if (i % 2 == 0 and n != i//2) or (i % 2 == 1 and n == i//2):
      # Check for A then B or B then A pattern
      if (i < 2*n and (i+1) % 2 != i % 2):
        movable_a.append(i)
        movable_a.append(i+1)
      elif (i > 1 and (i-1) % 2 != i % 2):
        movable_b.append(i-1)
        movable_b.append(i)

  # Initialize list to store moves
  moves = []

  # Move pairs to empty slots
  while movable_a or movable_b:
    if movable_a:
      # Find empty slot for A then B pair
      empty_slot = 0
      while empty_slot < -2*n + 1 and empty_slot + 1 < movable_a[0]:
        empty_slot += 2
      moves.append(f"from {movable_a[0]} to {empty_slot}")
      movable_a = [movable_a[1]] + [loc - 1 for loc in movable_a[2:]]
    else:
      # Find empty slot for B then A pair
      empty_slot = 0
      while empty_slot < -2*n + 1 and empty_slot + 1 < movable_b[0]:
        empty_slot += 2
      moves.append(f"from {movable_b[0]} to {empty_slot}")
      movable_b = [movable_b[1]] + [loc - 1 for loc in movable_b[2:]]

  return moves

# Get number of counters
n = int(input())

# Find and print moves to sort bins
moves = sort_baggage_bins(n)
for move in moves:
  print(move)
