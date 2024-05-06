# 8.6 Error 1/12
import sys

def frogger(n, board, magic):
  """Counts the number of winning instances of Frogger.

  Args:
    n: The number of board squares.
    board: A list of the numbers in the board squares in order from left to right.
    magic: The magic number for this instance of the game.

  Returns:
    The number of winning instances.
  """

  # Initialize the dp table.
  dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

  # Set the base cases.
  dp[0][0] = 1
  for i in range(1, n+1):
    dp[i][i] = 1 if board[i-1] == magic else 0

  # Fill in the dp table.
  for i in range(1, n+1):
    for j in range(i+1, n+1):
      if board[j-1] > 0:
        dp[i][j] = dp[i][j-board[j-1]]
      elif board[j-1] < 0:
        dp[i][j] = dp[i][j-abs(board[j-1])]

  # Return the number of winning instances.
  return dp[0][n]


if __name__ == "__main__":
  # Read the input.
  n = int(sys.stdin.readline())
  board = [int(x) for x in sys.stdin.readline().split()]
  magic = int(sys.stdin.readline())

  # Count the number of winning instances.
  num_winning_instances = frogger(n, board, magic)

  # Print the output.
  print(num_winning_instances)