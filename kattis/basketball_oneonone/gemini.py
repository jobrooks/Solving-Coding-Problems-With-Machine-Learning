# Difficulty: 1.5
# Result: Wrong Answer
# Tests passed: 0/16
# Error: none
# Response: 
def determine_winner(score_sequence):
  """
  Finds the winner of the one-on-one game based on scoring sequence.

  Args:
      score_sequence: String of 'A' and 'B' characters representing scores.

  Returns:
      A string: "A" if Alice wins, "B" if Bob wins.
  """

  alice_score = 0
  bob_score = 0
  possession = 'A'  # Start with Alice having possession

  for score in score_sequence:
    if possession == 'A':
      alice_score += 1
      if alice_score >= 11 and alice_score - bob_score >= 2:
        return 'A'  # Alice wins
      possession = score  # Possession changes only if Alice scores
    else:
      bob_score += 1
      if bob_score >= 11 and bob_score - alice_score >= 2:
        return 'B'  # Bob wins
      possession = score  # Possession changes only if Bob scores

  # Game ended without reaching 11 points or 2-point lead
  return 'B' if bob_score > alice_score else 'A'  # Winner is the one with higher score

# Get the sequence of scoring plays
score_sequence = input()

# Find and print the winner
winner = determine_winner(score_sequence)
print(winner)
