def add_em_up(cards, s):
  """
  Determines if two cards can be chosen such that (in some orientation) they add up to s.

  Args:
    cards: A list of integers representing the numbers on the cards.
    s: The desired sum.

  Returns:
    A string indicating whether or not two cards can be chosen to add up to s.
  """

  # Create a set of all the possible sums of two cards.
  sums = set()
  for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
      sums.add(cards[i] + cards[j])

  # Check if the desired sum is in the set of possible sums.
  if s in sums:
    return "YES"
  else:
    return "NO"


# Get the input.
n, s = map(int, input().split())
cards = list(map(int, input().split()))

# Print the output.
print(add_em_up(cards, s))