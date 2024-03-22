# 5.1 wrong answer 0/2
def is_valid_grid(grid):
    x_count = sum(row.count('X') for row in grid)
    o_count = sum(row.count('O') for row in grid)
    
    if x_count == o_count or x_count == o_count + 1:
        x_wins = any(all(cell == 'X' for cell in row) for row in grid) \
                 or any(all(grid[i][j] == 'X' for i in range(3)) for j in range(3)) \
                 or all(grid[i][i] == 'X' for i in range(3)) \
                 or all(grid[i][2-i] == 'X' for i in range(3))
        o_wins = any(all(cell == 'O' for cell in row) for row in grid) \
                 or any(all(grid[i][j] == 'O' for i in range(3)) for j in range(3)) \
                 or all(grid[i][i] == 'O' for i in range(3)) \
                 or all(grid[i][2-i] == 'O' for i in range(3))
        if x_wins and x_count != o_count + 1:
            return False
        elif o_wins and x_count != o_count:
            return False
        else:
            return True
    else:
        return False

# Example usage
grid = [['X', '.', '.',], ['O', 'X', 'O'], ['.', '.', '.',]]
print(is_valid_grid(grid)) # True

grid = [['X', '.', '.',], ['O', 'X', 'O'], ['.', '.', 'X']]
print(is_valid_grid(grid)) # True

grid = [['X', '.', '.',], ['O', 'X', 'O'], ['O', '.', '.',]]
print(is_valid_grid(grid)) # False
