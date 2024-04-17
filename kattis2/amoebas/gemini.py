def count_loops(grid):
    """Counts the number of closed loops in a rectangular grid of black and white pixels.

    Args:
        grid: A list of strings representing the grid, where '#' denotes a black pixel and '.' denotes a white pixel.

    Returns:
        The number of closed loops in the grid.
    """

    # Initialize the visited array to all False values.
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the loop count to 0.
    loop_count = 0

    # Iterate over each pixel in the grid.
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the pixel is black and has not been visited, perform a depth-first search to find all of the black pixels in the loop.
            if grid[i][j] == '#' and not visited[i][j]:
                loop_count += 1
                dfs(grid, visited, i, j)

    # Return the loop count.
    return loop_count


def dfs(grid, visited, i, j):
    """Performs a depth-first search to find all of the black pixels in a loop.

    Args:
        grid: A list of strings representing the grid, where '#' denotes a black pixel and '.' denotes a white pixel.
        visited: A list of lists of Boolean values indicating whether each pixel has been visited.
        i: The row index of the current pixel.
        j: The column index of the current pixel.
    """

    # Add the current pixel to the visited array.
    visited[i][j] = True

    # Iterate over the eight neighbors of the current pixel.
    for di in range(-1, 2):
        for dj in range(-1, 2):
            # If the neighbor is within the bounds of the grid and is black and has not been visited, perform a depth-first search on the neighbor.
            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]) and grid[i + di][j + dj] == '#' and not visited[i + di][j + dj]:
                dfs(grid, visited, i + di, j + dj)


def main():
    """Gets the input grid and prints the number of closed loops in the grid."""

    # Get the input grid.
    m, n = map(int, input().split())
    grid = [input() for _ in range(m)]

    # Count the number of closed loops in the grid.
    loop_count = count_loops(grid)

    # Print the number of closed loops in the grid.
    print(loop_count)


if __name__ == "__main__":
    main()