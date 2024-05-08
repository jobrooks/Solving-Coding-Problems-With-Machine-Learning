# 3.2 wrong answer 1/2
import random

def expected_prize(n, t):
  """
  Return the player's expected prize for a game with n questions and probability of answering correctly t.

  Args:
    n: The number of questions in the game.
    t: The probability of answering correctly.

  Returns:
    The player's expected prize.
  """

  # The player's expected prize for a game with i questions and probability of answering correctly t is:
  # p * (2 * expected_prize(i - 1, t)) + (1 - p) * 0
  # where p is the probability of answering correctly and 2 is the prize for answering correctly.

  if n == 0:
    return 0
  else:
    return t * (2 * expected_prize(n - 1, t)) + (1 - t) * 0

# Read the input.
input_lines = []
while True:
  line = input()
  if line == "0 0":
    break
  input_lines.append(line)

# Process the input.
for line in input_lines:
  n, t = map(float, line.split())
  print("{0:.3f}".format(expected_prize(n, t)))