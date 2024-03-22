# Difficulty: 3.2
# Justification: 
# Result: wrong answer
# Tests passed: 0/34
# Error: none
# Response: 
def min_rooms(minions):
  """
  Calculates the minimum number of rooms needed for minion temperature preferences.

  Args:
      minions: A list of tuples where each tuple represents a minion's preferred
                temperature range (lower bound, upper bound).

  Returns:
      The minimum number of rooms required.
  """
  # Sort minions by their lower bound temperatures
  minions.sort(key=lambda x: x[0])

  # Initialize variables for room assignment
  rooms = []
  current_room_end = -float("inf")

  for minion in minions:
    # Check if the minion's preferred range overlaps with the current room
    if minion[0] <= current_room_end:
      # Update the room end if the minion's upper bound extends further
      current_room_end = max(current_room_end, minion[1])
    else:
      # If no overlap, create a new room with this minion's range
      rooms.append(minion[1])
      current_room_end = minion[1]

  return len(rooms)

# Sample data (replace with actual input)
minions = [(2, 5), (1, 4), (3, 6)]

# Calculate and print the minimum number of rooms
min_rooms_needed = min_rooms(minions)
print(min_rooms_needed)
