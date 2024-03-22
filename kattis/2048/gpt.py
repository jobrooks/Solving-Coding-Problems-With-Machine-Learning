# 3.0 wrong answer 1/19

grid = []
for i in range(4):
    grid.append(list(map(int, input().split())))

move = int(input())

if move == 0:  # left
    for i in range(4):
        for j in range(1, 4):
            if grid[i][j] != 0:
                k = j
                while k > 0 and grid[i][k-1] == 0:
                    grid[i][k-1], grid[i][k] = grid[i][k], grid[i][k-1]
                    k -= 1
                if k > 0 and grid[i][k-1] == grid[i][k]:
                    grid[i][k-1] *= 2
                    grid[i][k] = 0

elif move == 1:  # up
    for j in range(4):
        for i in range(1, 4):
            if grid[i][j] != 0:
                k = i
                while k > 0 and grid[k-1][j] == 0:
                    grid[k-1][j], grid[k][j] = grid[k][j], grid[k-1][j]
                    k -= 1
                if k > 0 and grid[k-1][j] == grid[k][j]:
                    grid[k-1][j] *= 2
                    grid[k][j] = 0

elif move == 2:  # right
    for i in range(4):
        for j in range(2, -1, -1):
            if grid[i][j] != 0:
                k = j
                while k < 3 and grid[i][k+1] == 0:
                    grid[i][k+1], grid[i][k] = grid[i][k], grid[i][k+1]
                    k += 1
                if k < 3 and grid[i][k+1] == grid[i][k]:
                    grid[i][k+1] *= 2
                    grid[i][k] = 0

else:  # down
    for j in range(4):
        for i in range(2, -1, -1):
            if grid[i][j] != 0:
                k = i
                while k < 3 and grid[k+1][j] == 0:
                    grid[k+1][j], grid[k][j] = grid[k][j], grid[k+1][j]
                    k += 1
                if k < 3 and grid[k+1][j] == grid[k][j]:
                    grid[k+1][j] *= 2
                    grid[k][j] = 0

for row in grid:
    print(' '.join(map(str, row)))
