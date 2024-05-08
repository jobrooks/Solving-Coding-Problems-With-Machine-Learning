import sys
from math import sqrt

r, c, p = map(int, input().split())
ranges = list(map(int, input().split()))
grid = [list(input().split()) for _ in range(r)]
INF = sys.maxsize

# Find the starting position for the watchman
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'A':
            start_row, start_col = i, j
            break

# Initialize the distance grid
distance_grid = [[[INF] * (p + 1) for _ in range(c)] for _ in range(r)]
distance_grid[start_row][start_col][0] = 0

# Perform BFS to compute the shortest distance to each person
queue = [(start_row, start_col, 0)]
while queue:
    curr_row, curr_col, curr_person = queue.pop(0)
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_row, next_col = curr_row + dr, curr_col + dc
        if 0 <= next_row < r and 0 <= next_col < c:
            next_cost = distance_grid[curr_row][curr_col][curr_person] + int(grid[next_row][next_col])
            if next_cost < distance_grid[next_row][next_col][curr_person]:
                distance_grid[next_row][next_col][curr_person] = next_cost
                if grid[next_row][next_col] == chr(ord('A') + curr_person + 1):
                    queue.append((next_row, next_col, curr_person + 1))

# Check if all people can be reached
if distance_grid[start_row][start_col][p] == INF:
    print(-1)
else:
    print(distance_grid[start_row][start_col][p])