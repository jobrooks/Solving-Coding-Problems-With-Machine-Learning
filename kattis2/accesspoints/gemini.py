import sys
from collections import deque
from typing import List, Tuple

def main():
    n = int(input())
    access_points = [list(map(int, input().split())) for _ in range(n)]

    # Sort the access points by their x-coordinate
    access_points.sort(key=lambda x: x[0])

    # Create a deque to store the x-coordinates of the teams
    x_coordinates = deque()

    # Create a list to store the y-coordinates of the teams
    y_coordinates = []

    # Iterate over the access points
    for x, y in access_points:
        # If the team is the first team, or if the team's x-coordinate is greater than
        # the previous team's x-coordinate, add the team's x-coordinate to the deque
        if not x_coordinates or x > x_coordinates[-1]:
            x_coordinates.append(x)
            y_coordinates.append(deque())

        # Add the team's y-coordinate to the deque for its x-coordinate
        y_coordinates[-1].append(y)

    # Calculate the minimum total cost of all UTP cables
    total_cost = 0
    for x_coordinate in x_coordinates:
        y_coordinate = 0
        while y_coordinates:
            if not y_coordinates[0]:
                y_coordinates.popleft()
                continue

            y = y_coordinates[0].popleft()
            total_cost += (x_coordinate - y_coordinate) ** 2
            y_coordinate = y

    # Print the minimum total cost
    total_cost = round(total_cost, 6)
    print(total_cost)

if __name__ == "__main__":
    main()