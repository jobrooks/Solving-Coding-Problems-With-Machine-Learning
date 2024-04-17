def count_winning_instances(board, magic_number):
  """Counts the number of winning instances of a Frogger game.

  Args:
    board: A list of n integers representing the board squares.
    magic_number: The integer that the frog must land on to win.

  Returns:
    The number of winning instances.
  """

  # Create a dictionary to store the number of times each square has been visited.
  visited = {}
  for square in board:
    visited[square] = 0

  # Start the frog at the first square.
  position = 1

  # Keep playing until the frog wins or loses.
  while True:
    # Check if the frog has won.
    if board[position - 1] == magic_number:
      return 1

    # Check if the frog has lost.
    if position < 1 or position > len(board) or visited[board[position - 1]] >= 1:
      return 0

    # Mark the current square as visited.
    visited[board[position - 1]] += 1

    # Move the frog.
    position += board[position - 1]


# Read the input.
n = int(input())
board = [int(x) for x in input().split()]
magic_number = int(input())

# Count the number of winning instances.
count = 0
for starting_position in range(1, n + 1):
  count += count_winning_instances(board, magic_number)

# Print the output.
print(count)