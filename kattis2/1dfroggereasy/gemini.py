# 3.5 wrong answer 1/38
def is_valid(n, s, m, board):
    """
    Checks if the given Frogger game instance is valid.

    Args:
        n (int): Number of board squares.
        s (int): Index of the frog's starting square.
        m (int): Magic number.
        board (list): List of non-zero integers representing the numbers in the board squares.

    Returns:
        bool: True if the game instance is valid, False otherwise.
    """

    if not (1 <= n <= 200):
        return False
    if not (1 <= s <= n):
        return False
    if m not in board:
        return False
    for number in board:
        if not (-200 <= number <= 200):
            return False
    return True


def play_game(n, s, m, board):
    """
    Plays the Frogger game and returns the frog's fate and the number of hops it makes.

    Args:
        n (int): Number of board squares.
        s (int): Index of the frog's starting square.
        m (int): Magic number.
        board (list): List of non-zero integers representing the numbers in the board squares.

    Returns:
        tuple: A tuple containing the frog's fate (one of {'magic', 'left', 'right', 'cycle'}) and the number of hops it makes.
    """

    visited = set()
    fate = None
    num_hops = 0
    current_square = s

    while True:
        # Check if the frog has won.
        if current_square == m:
            fate = "magic"
            break

        # Check if the frog has fallen off the left end of the board.
        if current_square <= 1:
            fate = "left"
            break

        # Check if the frog has fallen off the right end of the board.
        if current_square >= n:
            fate = "right"
            break

        # Check if the frog has hopped onto a square where it has been before.
        if current_square in visited:
            fate = "cycle"
            break

        # Add the current square to the set of visited squares.
        visited.add(current_square)

        # Get the number on the current square.
        number = board[current_square - 1]

        # Increment the number of hops.
        num_hops += 1

        # Make the hop.
        if number > 0:
            current_square += number
        else:
            current_square -= abs(number)

    return fate, num_hops


def main():
    """
    Gets the input, validates it, and plays the Frogger game.
    """

    n, s, m = map(int, input().split())
    board = list(map(int, input().split()))

    if not is_valid(n, s, m, board):
        print("Invalid game instance.")
    else:
        fate, num_hops = play_game(n, s, m, board)
        print(fate)
        print(num_hops)


if __name__ == "__main__":
    main()