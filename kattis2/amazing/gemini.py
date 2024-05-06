import sys

maze = []
x = 0
y = 0
direction = "right"
visited = set()

def get_input():
  while True:
    line = sys.stdin.readline()
    if line == "wall\n":
      return "wall"
    elif line == "ok\n":
      return "ok"
    elif line == "solved\n":
      return "solved"
    elif line == "wrong\n":
      return "wrong"
    else:
      print("Invalid input")

def move(direction):
  global x, y
  if direction == "right":
    x += 1
  elif direction == "down":
    y += 1
  elif direction == "left":
    x -= 1
  elif direction == "up":
    y -= 1

def main():
  global maze, x, y, direction, visited

  # Read the first line of the maze
  line = sys.stdin.readline()
  while line != "":
    maze.append(line)
    line = sys.stdin.readline()

  # Get the starting position
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      if maze[i][j] == "S":
        x = j
        y = i
        break

  # Start the game loop
  while True:
    # Check if we have visited this cell before
    if (x, y) in visited:
      print("wrong\n")
      return

    # Mark the current cell as visited
    visited.add((x, y))

    # Get the input from the judging software
    response = get_input()

    # Check if we have solved the maze
    if response == "solved":
      print("solved\n")
      return

    # Check if we have hit a wall
    if response == "wall":
      # Change the direction based on the current direction
      if direction == "right":
        direction = "down"
      elif direction == "down":
        direction = "left"
      elif direction == "left":
        direction = "up"
      elif direction == "up":
        direction = "right"

      # Move one step in the new direction
      move(direction)
      continue

    # Move one step in the current direction
    move(direction)

if __name__ == "__main__":
  main()