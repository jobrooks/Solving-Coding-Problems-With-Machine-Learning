# Difficulty: 2.7
# Result: Wrong Answer
# Tests passed: 0/19
# Error: none
# Response: 
def generate_mech_counter(monster_moves):
  """
  Generates the mech counter moves for the monster's attack pattern.

  Args:
      monster_moves: String representing the monster's attack pattern (R, B, L).

  Returns:
      A string representing the mech counter moves (S, K, H, C).
  """

  mech_counter = ""
  combo = False  # Flag to track ongoing combo

  for move in monster_moves:
    if combo:
      # In a combo, Combo Breaker counters all remaining moves
      mech_counter += "C"
      combo = False
    else:
      # Standard counters for individual moves
      if move == "R":
        mech_counter += "S"
      elif move == "B":
        mech_counter += "K"
      elif move == "L":
        mech_counter += "H"
      else:
        raise ValueError("Invalid monster move:", move)
      # Check for combo after each move (except the last)
      if len(monster_moves) > 1 and monster_moves.index(move) < len(monster_moves) - 1:
        if (move in {"R", "B", "L"} and
            monster_moves[monster_moves.index(move) + 1] in {"R", "B", "L"} and
            monster_moves[monster_moves.index(move) + 2] in {"R", "B", "L"}):
          combo = True

  return mech_counter

# Get the monster's attack pattern
monster_moves = input()

# Generate and print the mech counter moves
mech_counter = generate_mech_counter(monster_moves)
print(mech_counter)
