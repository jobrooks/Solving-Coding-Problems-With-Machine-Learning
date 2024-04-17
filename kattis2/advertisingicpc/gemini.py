mod = 998244353

def get_num_ways(grid, n, m):
    """
    Counts the number of ways to fill the unfilled locations on the flag such that the flag is advertising ICPC.
    
    Args:
        grid (list): A 2D list representing the flag.
        n (int): The number of rows in the grid.
        m (int): The number of columns in the grid.
    
    Returns:
        int: The number of ways to fill the flag such that it is advertising ICPC, modulo 998244353.
    """

    # Check if the grid is already advertising ICPC.
    if is_advertising_icpc(grid):
        return 1

    # Get a list of all the unfilled locations on the grid.
    unfilled_locations = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "?":
                unfilled_locations.append((i, j))

    # Initialize the number of ways to fill the unfilled locations to 0.
    num_ways = 0

    # Try all possible ways to fill the unfilled locations.
    for i in range(3 ** len(unfilled_locations)):
        # Convert i to a ternary number.
        ternary_number = i
        filled_locations = []
        for j in range(len(unfilled_locations)):
            filled_locations.append(ternary_number % 3)
            ternary_number //= 3

        # Fill the unfilled locations with the corresponding letters.
        for j in range(len(unfilled_locations)):
            i, j = unfilled_locations[j]
            if filled_locations[j] == 0:
                grid[i][j] = "C"
            elif filled_locations[j] == 1:
                grid[i][j] = "I"
            else:
                grid[i][j] = "P"

        # Check if the grid is now advertising ICPC.
        if is_advertising_icpc(grid):
            num_ways += 1

        # Reset the grid to its original state.
        for j in range(len(unfilled_locations)):
            i, j = unfilled_locations[j]
            grid[i][j] = "?"

    # Return the number of ways to fill the unfilled locations.
    return num_ways % mod


def is_advertising_icpc(grid):
    """
    Checks if the grid is advertising ICPC.
    
    Args:
        grid (list): A 2D list representing the flag.
    
    Returns:
        bool: True if the grid is advertising ICPC, False otherwise.
    """

    n = len(grid)
    m = len(grid[0])

    # Check if there is at least one 2x2 subgrid that looks like the following:
    # IC
    # PC
    for i in range(n - 1):
        for j in range(m - 1):
            if grid[i][j] == "I" and grid[i + 1][j] == "C" and grid[i][j + 1] == "P" and grid[i + 1][j + 1] == "C":
                return True

    # Otherwise, the grid is not advertising ICPC.
    return False


# Read the input.
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))

# Count the number of ways to fill the flag such that it is advertising ICPC.
num_ways = get_num_ways(grid, n, m)

# Print the number of ways.
print(num_ways)