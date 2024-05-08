# 8.5 Error 1/2
def is_feasible(given_dice, desired_die):
  """
  Checks if it is possible to simulate the desired die using the given dice.

  Args:
    given_dice: A list of three lists, each representing a die. Each die is a list of
      three integers, representing the probabilities of rolling 1, 2, and 3, respectively.
    desired_die: A list of three integers, representing the probabilities of rolling
      1, 2, and 3, respectively, for the desired die.

  Returns:
    True if it is possible to simulate the desired die using the given dice, False
    otherwise.
  """

  for i in range(3):
    if desired_die[i] == 0:
      continue

    # Check if the desired probability is greater than the sum of the probabilities
    # of rolling the desired outcome on any of the given dice.
    if desired_die[i] > sum(die[i] for die in given_dice):
      return False

  return True


def main():
  test_cases = []

  # Read the test cases.
  while True:
    line = input()
    if line == '0 0 0':
      break

    test_cases.append([list(map(int, line.split())) for _ in range(4)])

  # Process the test cases.
  for test_case in test_cases:
    given_dice = test_case[:3]
    desired_die = test_case[3]

    if is_feasible(given_dice, desired_die):
      print('YES')
    else:
      print('NO')


if __name__ == '__main__':
  main()