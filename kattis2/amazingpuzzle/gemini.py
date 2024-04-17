import sys

# Read input
c, r, e = list(map(int, input().split()))
robots = list(map(int, input().split()))
walls_h = list(map(int, input().split()))
walls_v = list(map(int, input().split()))

# Convert robots' orientations to numbers
orientations = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
robots[2] = orientations[robots[2]]
robots[5] = orientations[robots[5]]

# Create a 2D array to represent the maze
maze = [[' ' for _ in range(c+1)] for _ in range(r+1)]

# Mark the exit
maze[1][e] = 'E'

# Mark the robots' starting positions
maze[robots[1]][robots[0]] = 'A'
maze[robots[4]][robots[3]] = 'B'

# Mark the walls
for i in range(0, len(walls_h), 2):
    maze[walls_h[i]][walls_h[i+1]] = '-'
for i in range(0, len(walls_v), 2):
    maze[walls_v[i]][walls_v[i+1]] = '|'

# Define the possible moves for each robot
moves = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

# Function to check if a move is valid
def is_valid(robot, move):
    x, y = robot[0] + move[0], robot[1] + move[1]
    return 0 <= x < r+1 and 0 <= y < c+1 and maze[x][y] != '-'

# Function to make a move
def move(robot, move):
    robot[0] += move[0]
    robot[1] += move[1]

# Function to rotate a robot left or right
def rotate(robot, direction):
    if direction == 'L':
        robot[2] = (robot[2] - 1) % 4
    else:
        robot[2] = (robot[2] + 1) % 4

# Function to find the minimum number of moves to get both robots out of the maze
def solve(robots):
    # Initialize the queue with the initial state
    queue = [(robots, 0, 0)]

    # Keep track of the visited states
    visited = set()

    # While there are states to explore
    while queue:
        # Get the current state
        state, moves, bumps = queue.pop(0)
        robots_a, robots_b = state

        # Check if the current state is a goal state
        if robots_a[0] == 1 or robots_b[0] == 1:
            return moves, bumps

        # If the current state has not been visited
        if state not in visited:
            # Mark the current state as visited
            visited.add(state)

            # Try all possible moves for robot A
            for move in moves[orientations[robots_a[2]]]:
                # If the move is valid
                if is_valid(robots_a, move):
                    # Make the move
                    move(robots_a, move)

                    # If the move results in a bump
                    if maze[robots_a[0]][robots_a[1]] == '|':
                        bumps += 1

                    # Add the new state to the queue
                    queue.append(((robots_a, robots_b), moves+1, bumps))

                    # Undo the move
                    move(robots_a, (-move[0], -move[1]))

            # Try all possible moves for robot B
            for move in moves[orientations[robots_b[2]]]:
                # If the move is valid
                if is_valid(robots_b, move):
                    # Make the move
                    move(robots_b, move)

                    # If the move results in a bump
                    if maze[robots_b[0]][robots_b[1]] == '|':
                        bumps += 1

                    # Add the new state to the queue
                    queue.append(((robots_a, robots_b), moves+1, bumps))

                    # Undo the move
                    move(robots_b, (-move[0], -move[1]))

    # If no solution was found
    return -1, -1

# Solve the maze
moves, bumps = solve(robots)

# Output the results
print(moves, bumps)