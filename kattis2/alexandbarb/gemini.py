import sys

def nim_sum(n):
  result = 0
  while n > 0:
    result ^= n
    n //= 2
  return result

def main():
  # Read input
  k, m, n = map(int, sys.stdin.readline().split())

  # Compute the nim-sum of the range [m, n]
  nim = nim_sum(m) ^ nim_sum(n + 1)

  # Determine the winner
  if nim == 0:
    winner = "Barb"
  else:
    winner = "Alex"

  # Print the winner
  print(winner)

if __name__ == "__main__":
  main()