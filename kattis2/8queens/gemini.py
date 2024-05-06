# 2.9 wrong answer 6/86
# Read the chess board from user input
board = [input() for _ in range(8)]

# Check if there are more than 8 queens on the board
queens = 0
for row in board:
    queens += row.count('*')

if queens != 8:
    print("invalid")
    exit()

# Check if any two queens can attack each other
for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            # Check the same row
            for k in range(j+1, 8):
                if board[i][k] == '*':
                    print("invalid")
                    exit()
            # Check the same column
            for k in range(i+1, 8):
                if board[k][j] == '*':
                    print("invalid")
                    exit()
            # Check the diagonals
            for k in range(1, 8):
                if 0 <= i-k < 8 and 0 <= j-k < 8 and board[i-k][j-k] == '*':
                    print("invalid")
                    exit()
                if 0 <= i+k < 8 and 0 <= j+k < 8 and board[i+k][j+k] == '*':
                    print("invalid")
                    exit()

# If we reach this point, the chess board is a valid solution
print("valid")