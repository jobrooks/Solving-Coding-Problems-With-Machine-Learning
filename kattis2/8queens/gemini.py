# 2.9 Error 3/86
board = [input() for _ in range(8)]

for i in range(8):
    for j in range(8):
        if board[i][j] == '*':
            # Check the row
            if '*' in board[i][:j] or '*' in board[i][j+1:]:
                print("invalid")
                exit()

            # Check the column
            for k in range(8):
                if board[k][j] == '*' and k != i:
                    print("invalid")
                    exit()

            # Check the diagonals
            for k, l in zip(range(i, -1, -1), range(j, -1, -1)):
                if board[k][l] == '*' and (k, l) != (i, j):
                    print("invalid")
                    exit()

            for k, l in zip(range(i, -1, -1), range(j, 8)):
                if board[k][l] == '*' and (k, l) != (i, j):
                    print("invalid")
                    exit()

            for k, l in zip(range(i, 8), range(j, -1, -1)):
                if board[k][l] == '*' and (k, l) != (i, j):
                    print("invalid")
                    exit()

            for k, l in zip(range(i, 8), range(j, 8)):
                if board[k][l] == '*' and (k, l) != (i, j):
                    print("invalid")
                    exit()

print("valid")