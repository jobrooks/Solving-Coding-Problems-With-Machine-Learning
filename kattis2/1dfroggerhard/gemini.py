# 8.6 wrong answer 1/12
import sys

def main():
  # Read the input.
  n = int(sys.stdin.readline())
  board = [int(x) for x in sys.stdin.readline().split()]

  # Create a dictionary to store the number of times each square has been visited.
  visited = {}

  # Count the number of winning instances.
  count = 0
  for start in range(1, n + 1):
    for magic in range(1, n + 1):
      if play(start, magic, board, visited):
        count += 1

  # Print the output.
  print(count)

def play(start, magic, board, visited):
  """
  Plays a game of Frogger.

  Args:
    start: The starting position of the frog.
    magic: The magic number.
    board: The board.
    visited: A dictionary to store the number of times each square has been visited.

  Returns:
    True if the game is won, False otherwise.
  """

  # Check if the game has already been played.
  if start in visited:
    return False

  # Update the number of times the square has been visited.
  visited[start] = visited.get(start, 0) + 1

  # Check if the game has been won.
  if start == magic:
    return True

  # Check if the game has been lost.
  if start < 1 or start > len(board):
    return False

  # Check if the frog is trapped in a cycle.
  if visited[start] > 1:
    return False

  # Make a hop.
  hop = board[start - 1]
  if hop > 0:
    return play(start + hop, magic, board, visited)
  else:
    return play(start - abs(hop), magic, board, visited)

if __name__ == "__main__":
  main()