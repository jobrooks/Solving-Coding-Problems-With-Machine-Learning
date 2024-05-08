def count_loops(grid):
  """Counts the number of closed loops in a rectangular array of black and white pixels.

  Args:
    grid: A 2D array of characters representing the grid.

  Returns:
    The number of closed loops in the grid.
  """

  def dfs(i, j):
    """Performs a depth-first search to find all the pixels in a loop.

    Args:
      i: The row index of the current pixel.
      j: The column index of the current pixel.
    """
    # Mark the current pixel as visited.
    grid[i][j] = '.'

    # Check if the current pixel is part of a loop.
    if (i == 0 or grid[i - 1][j] == '.') and (j == 0 or grid[i][j - 1] == '.'):
      return True

    # Recursively search the neighbors of the current pixel.
    return dfs(i - 1, j) or dfs(i + 1, j) or dfs(i, j - 1) or dfs(i, j + 1)

  # Count the number of loops in the grid.
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '#' and dfs(i, j):
        count += 1

  return count


def main():
  # Get the input grid.
  m, n = map(int, input().split())
  grid = [list(input()) for _ in range(m)]

  # Count the number of loops in the grid.
  count = count_loops(grid)

  # Print the number of loops.
  print(count)


if __name__ == "__main__":
  main()