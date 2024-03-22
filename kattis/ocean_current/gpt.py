# 5.0 wrong answer 0/4
import heapq

# Define the weights of the edges depending on the direction of the current
directions = [
    (-1, 0), # north
    (-1, 1), # northeast
    (0, 1),  # east
    (1, 1),  # southeast
    (1, 0),  # south
    (1, -1), # southwest
    (0, -1), # west
    (-1, -1) # northwest
]
weights = [[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        dx = directions[i][0] - directions[j][0]
        dy = directions[i][1] - directions[j][1]
        if dx == 0 and dy == 0:
            weights[i][j] = 0
        elif dx == 0 or dy == 0:
            weights[i][j] = 1
        else:
            weights[i][j] = 2

# Read input
n_rows, n_cols = map(int, input().split())
grid = [input() for _ in range(n_rows)]
n_trips = int(input())
trips = [tuple(map(int, input().split())) for _ in range(n_trips)]

def to_node(row, col):
    return row*n_cols + col

def to_coord(node):
    return node // n_cols, node % n_cols

def neighbors(node):
    row, col = to_coord(node)
    for i, (dx, dy) in enumerate(directions):
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < n_rows and 0 <= new_col < n_cols:
            yield to_node(new_row, new_col), weights[i][int(grid[row][col])]

def dijkstra(source, dest):
    queue = [(0, source)]
    visited = [False] * (n_rows * n_cols)
    dist = [float('inf')] * (n_rows * n_cols)
    dist[source] = 0
    while queue:
        d, node = heapq.heappop(queue)
        if node == dest:
            return d
       
