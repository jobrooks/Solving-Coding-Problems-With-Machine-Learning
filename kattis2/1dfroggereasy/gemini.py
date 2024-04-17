import sys

def main():
    # Read input
    n, s, m = map(int, sys.stdin.readline().split())
    board = list(map(int, sys.stdin.readline().split()))

    # Initialize frog's position and hop count
    pos = s
    h = 0

    # Keep track of visited squares to detect cycles
    visited = set()

    # Game loop
    while True:
        # Check if the frog has won
        if board[pos - 1] == m:
            print('magic')
            print(h)
            return

        # Check if the frog has fallen off the board
        if pos < 1 or pos > n:
            if pos < 1:
                print('left')
            else:
                print('right')
            print(h)
            return

        # Check if the frog has entered a cycle
        if pos in visited:
            print('cycle')
            print(h)
            return

        # Mark the current square as visited
        visited.add(pos)

        # Move the frog
        pos += board[pos - 1]

        # Increment the hop count
        h += 1

# Call the main function
if __name__ == '__main__':
    main()