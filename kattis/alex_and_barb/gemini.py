# Difficulty: 3.8
# Justification: 
# Result: wrong answer
# Tests passed: 1/13
# Error: none
# Response: 
def winning_player(k, m, n):
  """
  Determines the winner of the card game based on optimal strategy.

  Args:
      k: The number of cards in the stack (1 <= k <= 10^9).
      m: The minimum number of cards a player can take (1 <= m <= n <= 10^9).
      n: The maximum number of cards a player can take (1 <= m <= n <= 10^9).

  Returns:
      A string "Alex" or "Barb" indicating the winning player.
  """

  # Base case: If only 1 card remains, the next player loses
  if k == 1:
    return "Barb" if k % 2 == 1 else "Alex"  # Alex starts, so loses on odd remaining cards

  # Winning condition: Leave the opponent with a losing position (1 card)
  winning_positions = set(range(m, n + 1))  # Set of possible winning positions (k - cards taken)
  for x in range(m, n + 1):
    # Check if taking x cards leaves the opponent with a losing position
    remaining = k - x
    if remaining not in winning_positions:
      winning_positions.add(remaining)  # This position is a win for the current player

  # Alex starts, so wins if the initial position (k cards) is winning
  return "Alex" if k in winning_positions else "Barb"

# Example usage (replace with actual input)
k = 10
m = 2
n = 3
winner = winning_player(k, m, n)
print(winner)
