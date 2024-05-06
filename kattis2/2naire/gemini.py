# 3.2 Error 1/2
import sys

def expected_prize(n, t):
  """Returns the player's expected prize, if he plays the best strategy.

  Args:
    n: The number of questions.
    t: The minimum probability of answering a question correctly.

  Returns:
    The player's expected prize.
  """

  # The player's expected prize is the sum of the expected prizes for each
  # question.
  expected_prize = 0
  for i in range(n):
    # The player's expected prize for question i is the probability of
    # answering the question correctly times the prize for answering the
    # question correctly, plus the probability of answering the question
    # incorrectly times the prize for answering the question incorrectly.
    expected_prize += (1 - t) * 1 + t * (2 ** i)

  return expected_prize


def main():
  # Read the input.
  for line in sys.stdin:
    n, t = map(float, line.split())
    if n == 0 and t == 0:
      break

    # Compute the player's expected prize.
    expected_prize = expected_prize(n, t)

    # Print the player's expected prize.
    print("{:.3f}".format(expected_prize))


if __name__ == "__main__":
  main()