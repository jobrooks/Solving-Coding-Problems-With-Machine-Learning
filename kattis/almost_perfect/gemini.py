# Difficulty: 3.0
# Justification: 
# Result: passed
# Tests passed: 2/2
# Error: none
# Response: 
def is_almost_perfect(n):
  """
  Checks if a number is perfect, almost perfect, or not perfect.

  Args:
      n: A positive integer (2 <= n <= 10^9).

  Returns:
      A string indicating if n is "perfect", "almost perfect", or "not perfect".
  """
  sum_of_divisors = 1  # Initialize with 1 (divisor 1)
  for i in range(2, int(n**0.5) + 1):  # Check divisors up to the square root of n
    if n % i == 0:
      sum_of_divisors += i
      if i * i != n:  # If n is not a perfect square, add the other divisor
        sum_of_divisors += n // i

  if sum_of_divisors == n:
    return "perfect"
  elif abs(sum_of_divisors - n) <= 2:
    return "almost perfect"
  else:
    return "not perfect"

# Read input until end of file (EOF)
while True:
  try:
    n = int(input())
    result = is_almost_perfect(n)
    print(f"{n} {result}")
  except EOFError:
    break
