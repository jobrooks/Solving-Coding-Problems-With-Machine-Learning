import sys

def binomial_coefficient(n, k):
  """
  Computes the binomial coefficient of n choose k.

  Args:
    n: The first number in the binomial coefficient.
    k: The second number in the binomial coefficient.

  Returns:
    The binomial coefficient of n choose k.
  """

  if k < 0 or k > n:
    return 0
  if k == 0 or k == n:
    return 1
  return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def main():
  """
  Gets the input from the user and prints the output.
  """

  # Get the input from the user.
  x = int(input())

  # Find the smallest n and k such that n choose k equals x.
  n = 1
  k = 0
  while binomial_coefficient(n, k) != x:
    if binomial_coefficient(n, k) < x:
      k += 1
    else:
      n += 1

  # Print the output.
  print(n, k)

if __name__ == "__main__":
  main()