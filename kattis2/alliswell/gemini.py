import sys
import heapq

def dijkstra(grid, start, end, hearing_ranges):
  """
  Dijkstra's algorithm to find the shortest path from start to end.

  Args:
    grid: A 2D grid of weights.
    start: The starting cell.
    end: The ending cell.
    hearing_ranges: A dictionary of person letters to their hearing ranges.

  Returns:
    The shortest path from start to end, or -1 if no path exists.
  """

  # Initialize the distance to each cell to infinity.
  distance = {}
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      distance[(row, col)] = float('inf')

  # Set the distance to the starting cell to 0.
  distance[start] = 0

  # Initialize the priority queue with the starting cell.
  pq = [(0, start)]

  # While the priority queue is not empty,
  while pq:

    # Get the cell with the smallest distance from the priority queue.
    dist, cell = heapq.heappop(pq)

    # If this cell is the end cell,
    if cell == end:
      # Return the distance.
      return dist

    # For each neighbor of the cell,
    for neighbor in [(cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]),
                    (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)]:

      # If the neighbor is within the grid,
      if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):

        # If the neighbor is not an obstacle,
        if grid[neighbor[0]][neighbor[1]] != 'X':

          # If the neighbor is a person,
          if grid[neighbor[0]][neighbor[1]] in hearing_ranges:

            # If the distance to the neighbor is greater than the distance to the
            # current cell plus the time it takes to enter the neighbor,
            if distance[neighbor] > dist + grid[neighbor[0]][neighbor[1]]:

              # Update the distance to the neighbor.
              distance[neighbor] = dist + grid[neighbor[0]][neighbor[1]]

              # Add the neighbor to the priority queue.
              heapq.heappush(pq, (distance[neighbor], neighbor))

  # If no path was found,
  return -1

def main():

  # Read the input.
  r, c, p = map(int, input().split())
  hearing_ranges = {}
  for i in range(p):
    hearing_ranges[chr(ord('A') + i)] = int(input())
  grid = []
  for i in range(r):
    grid.append(input().split())

  # Find the starting cell.
  for i in range(r):
    for j in range(c):
      if grid[i][j] == 'A':
        start = (i, j)

  # Find the ending cell.
  for i in range(r):
    for j in range(c):
      if grid[i][j] == 'Z':
        end = (i, j)

  # Find the shortest path from the starting cell to the ending cell.
  dist = dijkstra(grid, start, end, hearing_ranges)

  # Print the output.
  if dist == -1:
    print(-1)
  else:
    print(dist)

if __name__ == "__main__":
  main()