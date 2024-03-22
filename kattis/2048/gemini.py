# Difficulty: 3.1
# Justification: none
# Result: failed
# Tests passed: 0/19
# Error: none
# Response: 
def move_left(grid):
  """
  Moves tiles left and merges them if possible.

  Args:
      grid: A list of lists representing the 4x4 grid.

  Returns:
      A new grid with the updated state after moving left.
  """
  new_grid = [[0 for _ in range(4)] for _ in range(4)]
  for row in range(4):
    non_zero_tiles = []
    for col in range(4):
      if grid[row][col] != 0:
        non_zero_tiles.append(grid[row][col])
    merged = False
    new_col = 0
    for tile in non_zero_tiles:
      if new_col == 0 or new_col == len(non_zero_tiles) - 1 or non_zero_tiles[new_col] != non_zero_tiles[new_col - 1]:
        new_grid[row][new_col] = tile
      else:
        new_grid[row][new_col - 1] *= 2
        merged = True
      if not merged:
        new_col += 1
  return new_grid

def move_right(grid):
  """
  Moves tiles right and merges them if possible.

  Args:
      grid: A list of lists representing the 4x4 grid.

  Returns:
      A new grid with the updated state after moving right.
  """
  return move_left([row[::-1] for row in grid])[::-1]

def move_up(grid):
  """
  Moves tiles up and merges them if possible.

  Args:
      grid: A list of lists representing the 4x4 grid.

  Returns:
      A new grid with the updated state after moving up.
  """
  return transpose(move_left(transpose(grid)))

def move_down(grid):
  """
  Moves tiles down and merges them if possible.

  Args:
      grid: A list of lists representing the 4x4 grid.

  Returns:
      A new grid with the updated state after moving down.
  """
  return transpose(move_right(transpose(grid)))

def transpose(grid):
  """
  Transposes the grid (swaps rows and columns).

  Args:
      grid: A list of lists representing the 4x4 grid.

  Returns:
      The transposed grid.
  """
  return [[row[i] for row in grid] for i in range(4)]

def has_empty_cells(grid):
  """
  Checks if the grid has any empty cells.

  Args:
      grid: A list of lists representing the 4x4 grid.

  Returns:
      True if there are empty cells, False otherwise.
  """
  for row in grid:
    for cell in row:
      if cell == 0:
        return True
  return False

def can_merge(grid, direction):
  """
  Checks if tiles can be merged in the given direction.

  Args:
      grid: A list of lists representing the 4x4 grid.
      direction: An integer representing the direction (0: left, 1: up, 2: right, 3: down)

  Returns:
      True if tiles can be merged, False otherwise.
  """
  new_grid = move(grid, direction)
  return new_grid != grid

def move(grid, direction):
  """
  Moves tiles in the specified direction and merges them.

  Args:
      grid: A list of lists representing the 4x4 grid.
      direction: An integer representing the direction (0: left, 1: up, 2: right, 3: down)

  Returns:
      A new grid with the updated state after the move.
  """
  move_functions = {0: move_left, 1: move_up, 2: move_right, 3: move_down}
  return move_functions[direction](grid.copy())

def play(grid, direction):
  """
  Simulates a move in the 2048 game and returns the new grid, game over status, and formatted output.

  Args:
      grid: A list of lists representing the 4x4 grid.
      direction: An integer representing the direction (0: left, 1: up, 2: right, 3: down)

  Returns:
      A tuple containing the new grid, a boolean indicating if the game has ended, and a string representing the formatted output.
  """
  new_grid, game_over = move(grid, direction)
  # Check if a 2048 tile exists
  for row in new_grid:
    for cell in row:
      if cell == 2048:
        game_over = False
  
  # Format output
  output = ""
  for row in new_grid:
    output += " ".join(str(x) for x in row) + "\n"
  
  return new_grid, game_over, output


