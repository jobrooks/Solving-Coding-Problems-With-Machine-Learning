# Difficulty: 4.2
# Justification: 
# Result: wrong answer
# Tests passed: 0/35
# Error: none
# Response: 
def next_animal_move(previous, unused_animals):
  """
  Finds the best next animal name to play in the alphabet animal game.

  Args:
      previous: The animal name said by the previous player (string).
      unused_animals: A list of unused animal names (strings).

  Returns:
      A string containing the next animal name to play (or "?" if no valid move).
  """

  last_letter = previous[-1]
  for animal in unused_animals:
    # Check if animal starts with the same letter as previous ends with
    if animal[0] == last_letter:
      # Eliminate the next player if no other animal starts with the chosen letter
      if all(animal[0] != a[0] for a in unused_animals if a != animal):
        return animal + "!"  # Return with exclamation mark to indicate elimination
      else:
        return animal  # Return the valid animal name

  # No valid move found
  return "?"

# Read input
previous_animal = input()
num_animals = int(input())
unused_animals = [input() for _ in range(num_animals)]

# Find the next move
next_move = next_animal_move(previous_animal, unused_animals)
print(next_move)
