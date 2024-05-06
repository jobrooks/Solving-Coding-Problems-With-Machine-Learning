import sys

def frogger(n, s, m, board):
    """
    Simulates the Frogger game.

    Parameters:
    n: The number of board squares.
    s: The index of the frog's starting square.
    m: The magic number.
    board: A list of the numbers in the board squares.

    Returns:
    A tuple of the frog's fate and the number of hops the frog makes before encountering its fate.
    """

    # Initialize the frog's position and the number of hops.
    position = s
    hops = 0

    # Create a set of the squares that the frog has visited.
    visited = set()

    # Loop until the frog encounters its fate.
    while True:

        # Increment the number of hops.
        hops += 1

        # Get the number in the square where the frog is.
        number = board[position - 1]

        # If the frog is on a square containing the magic number, the frog wins.
        if number == m:
            return 'magic', hops

        # If the frog is on a square containing a positive integer, the frog makes a length-k hop to the right.
        elif number > 0:
            position += number

        # If the frog is on a square containing a negative integer, the frog makes a length-|k| hop to the left.
        else:
            position -= abs(number)

        # If the frog falls off the left end of the board, the frog loses.
        if position < 1:
            return 'left', hops

        # If the frog falls off the right end of the board, the frog loses.
        elif position > n:
            return 'right', hops

        # If the frog hops onto a square where the frog has been before, the frog is trapped in a cycle.
        if position in visited:
            return 'cycle', hops

        # Add the frog's current position to the set of visited squares.
        visited.add(position)


# Read the input.
n, s, m = map(int, input().split())
board = list(map(int, input().split()))

# Simulate the game.
fate, hops = frogger(n, s, m, board)

# Print the output.
print(fate)
print(hops)