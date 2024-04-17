import sys

# Define the directions
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

# Initialize the maze
maze = []

# Get the maze from the input
for line in sys.stdin:
    maze.append(line.strip())

# Find the starting position
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == "S":
            start_i = i
            start_j = j

# Create a stack to store the path
path = []

# Define the function to move in a direction
def move(direction):
    global start_i, start_j, path, maze

    if direction == UP:
        start_i -= 1
    elif direction == DOWN:
        start_i += 1
    elif direction == LEFT:
        start_j -= 1
    elif direction == RIGHT:
        start_j += 1

    # Check if the move is valid
    if start_i < 0 or start_i >= len(maze) or start_j < 0 or start_j >= len(maze[0]):
        print("wrong")
        sys.exit()

    # Check if the move is a wall
    if maze[start_i][start_j] == "*":
        print("wall")
    # Check if the move is a solution
    elif maze[start_i][start_j] == "E":
        print("solved")
        sys.exit()
    # Check if the move has already been made
    elif (start_i, start_j) in path:
        print("wrong")
        sys.exit()
    # Otherwise, add the move to the path and continue
    else:
        path.append((start_i, start_j))
        print("ok")

# While the maze has not been solved
while True:
    # Get the direction from the input
    direction = input()

    # Move in the direction
    move(direction)