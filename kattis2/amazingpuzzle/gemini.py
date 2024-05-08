from collections import deque
from queue import PriorityQueue

def main():
  # Read the maze dimensions, exit location, and robot starting positions and orientations
  c, r, e = map(int, input().split())
  c1, r1, d1, c2, r2, d2 = input().split()
  c1, r1, c2, r2 = int(c1), int(r1), int(c2), int(r2)

  # Read the horizontal and vertical walls
  horizontal_walls = set()
  vertical_walls = set()
  for _ in range(int(input())):
    c1, r1, c2, r2 = map(int, input().split())
    horizontal_walls.add((c1, r1))

  for _ in range(int(input())):
    c1, r1, c2, r2 = map(int, input().split())
    vertical_walls.add((c1, r1))

  # Create a graph to represent the maze
  graph = {}
  for i in range(1, c + 1):
    for j in range(1, r + 1):
      graph[(i, j)] = set()

  # Add edges to the graph based on the walls
  for (c1, r1) in horizontal_walls:
    graph[(c1, r1)].add((c1, r1 + 1))
    graph[(c1, r1 + 1)].add((c1, r1))

  for (c1, r1) in vertical_walls:
    graph[(c1, r1)].add((c1 + 1, r1))
    graph[(c1 + 1, r1)].add((c1, r1))

  # Define the possible robot orientations and movements
  orientations = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
  movements = {"F": (0, 0), "L": (-1, 0), "R": (1, 0)}

  # Perform a breadth-first search to find the minimum number of forward commands to get both robots out of the maze
  queue = deque([(c1, r1, d1, c2, r2, d2, 0, 0)])
  visited = set()
  min_forward_commands = float('inf')
  min_bumps = float('inf')

  while queue:
    c1, r1, d1, c2, r2, d2, forward_commands, bumps = queue.popleft()

    if (c1, r1) == (e, 1) or (c2, r2) == (e, 1):
      if forward_commands < min_forward_commands or (forward_commands == min_forward_commands and bumps < min_bumps):
        min_forward_commands = forward_commands
        min_bumps = bumps

    if (c1, r1, d1, c2, r2, d2) in visited:
      continue

    visited.add((c1, r1, d1, c2, r2, d2))

    # Try all possible movements for both robots
    for command in ["F", "L", "R"]:
      # Get the new positions and orientations of the robots
      c1_new, r1_new = c1 + movements[command][0] * orientations[d1][0], r1 + movements[command][0] * orientations[d1][1]
      c2_new, r2_new = c2 + movements[command][0] * orientations[d2][0], r2 + movements[command][0] * orientations[d2][1]
      d1_new = d1 if command != "L" and command != "R" else orientations[d1][1]
      d2_new = d2 if command != "L" and command != "R" else orientations[d2][1]

      # Check if the new positions are valid and not occupied by the other robot
      if (c1_new, r1_new) not in graph or (c1_new, r1_new) == (c2, r2):
        continue
      if (c2_new, r2_new) not in graph or (c2_new, r2_new) == (c1, r1):
        continue

      # Add the new state to the queue
      queue.append((c1_new, r1_new, d1_new, c2_new, r2_new, d2_new, forward_commands + (command == "F"), bumps + (command == "F" and ((c1_new, r1_new) in horizontal_walls or (c2_new, r2_new) in horizontal_walls or (c1_new, r1_new) in vertical_walls or (c2_new, r2_new) in vertical_walls))))

  # Print the minimum number of forward commands and the number of bumps
  print(min_forward_commands, min_bumps)

if __name__ == "__main__":
  main()