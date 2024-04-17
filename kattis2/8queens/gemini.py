def is_valid_chessboard(chessboard):
  """
  Checks if the given chessboard is a valid solution to the eight queens puzzle.

  Args:
    chessboard: A list of lists of characters representing the chessboard.

  Returns:
    True if the chessboard is valid, False otherwise.
  """

  # Check if the chessboard is the correct size.
  if len(chessboard) != 8 or any(len(row) != 8 for row in chessboard):
    return False

  # Check if there are more than 8 queens on the board.
  num_queens = sum(1 for row in chessboard for cell in row if cell == '*')
  if num_queens != 8:
    return False

  # Check if any queen can attack another queen.
  for row in range(8):
    for col in range(8):
      if chessboard[row][col] == '*':
        # Check if there is a queen in the same row.
        for other_col in range(8):
          if other_col != col and chessboard[row][other_col] == '*':
            return False

        # Check if there is a queen in the same column.
        for other_row in range(8):
          if other_row != row and chessboard[other_row][col] == '*':
            return False

        # Check if there is a queen in the same diagonal.
        for other_row in range(1, 8):
          if row + other_row < 8 and col + other_row < 8 and chessboard[row + other_row][col + other_row] == '*':
            return False

          if row - other_row >= 0 and col + other_row < 8 and chessboard[row - other_row][col + other_row] == '*':
            return False

  # If all checks pass, the chessboard is valid.
  return True


def main():
  """
  Gets the chessboard from the user and prints whether or not it is a valid solution to the eight queens puzzle.
  """

  # Get the chessboard from the user.
  chessboard = []
  for _ in range(8):
    chessboard.append(list(input()))

  # Check if the chessboard is valid.
  if is_valid_chessboard(chessboard):
    print("valid")
  else:
    print("invalid")


if __name__ == "__main__":
  main()