# 6.9 Error 1/9
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
desired = [list(map(int, input().split())) for _ in range(r)]

# Construct a sorted list of all heights in the grid
heights = sorted(set([item for row in grid for item in row]))

# Create a dictionary to map each height to its corresponding coordinates in the grid
pos = {}
for i in range(r):
    for j in range(c):
        pos[grid[i][j]] = (i, j)

# Function to perform a swap between two students
def swap(i1, j1, i2, j2):
    grid[i1][j1], grid[i2][j2] = grid[i2][j2], grid[i1][j1]

# Perform swaps until the desired arrangement is achieved
k = 0
while grid != desired:
    # Find the minimum height that is not in its desired position
    h = min([h for h in heights if pos[h] != desired[pos[h][0]][pos[h][1]]])

    # Swap the student with minimum height with the student in its desired position
    i, j = pos[h]
    i_d, j_d = desired[i][j]
    swap(i, j, i_d, j_d)

    # Update the position of the swapped students
    pos[grid[i][j]] = (i, j)
    pos[grid[i_d][j_d]] = (i_d, j_d)
    
    k += 1

print(k)
for _ in range(k):
    i1, j1, i2, j2 = map(int, input().split())
    swap(i1 - 1, j1 - 1, i2 - 1, j2 - 1)