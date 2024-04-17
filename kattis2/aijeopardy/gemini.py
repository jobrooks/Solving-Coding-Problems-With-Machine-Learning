import math

def binomial(x):
  """Returns a tuple (n, k) representing the most elegant binomial coefficient for x.
  
  The most elegant solution has the smallest value of n, and of those with the smallest
  n it should choose the one with the smallest value of k.

  Args:
    x: A positive integer.

  Returns:
    A tuple (n, k) such that n choose k equals x, with ties broken as explained
    above.
  """

  # Find the largest integer n such that n choose 1 <= x.

  n = 1
  while n * (n + 1) <= x * 2:
    n += 1

  # Find the largest integer k such that n choose k <= x.

  k = n - 1
  while math.factorial(n) / (math.factorial(k) * math.factorial(n - k)) <= x:
    k += 1

  return (n, k)


def main():
  """Gets an integer x from the user and prints its most elegant binomial coefficient."""

  x = int(input())
  n, k = binomial(x)
  print(n, k)


if __name__ == "__main__":
  main()