import math

# Get the coordinates of the starting and ending points.
x_a, y_a, x_b, y_b = map(float, input().split())

# Get the number of conveyors.
n = int(input())

# Get the coordinates of the start and end points of each conveyor.
conveyors = []
for _ in range(n):
    x1, y1, x2, y2 = map(float, input().split())
    conveyors.append(((x1, y1), (x2, y2)))

# Initialize the distance to the starting point.
distance = math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2)

# Find the shortest path to the ending point.
for conveyor in conveyors:
    # Check if the starting point is on the conveyor.
    if (x_a, y_a) in conveyor:
        # Check if the ending point is on the conveyor.
        if (x_b, y_b) in conveyor:
            # Calculate the distance on the conveyor.
            distance_on_conveyor = math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2) / 2
            # Update the distance.
            distance = min(distance, distance_on_conveyor)
        else:
            # Calculate the distance to the end of the conveyor.
            distance_to_end = math.sqrt((x2 - x_a)**2 + (y2 - y_a)**2) / 2
            # Calculate the distance from the end of the conveyor to the ending point.
            distance_from_end = math.sqrt((x_b - x2)**2 + (y_b - y2)**2)
            # Update the distance.
            distance = min(distance, distance_to_end + distance_from_end)
    else:
        # Check if the ending point is on the conveyor.
        if (x_b, y_b) in conveyor:
            # Calculate the distance to the start of the conveyor.
            distance_to_start = math.sqrt((x1 - x_b)**2 + (y1 - y_b)**2) / 2
            # Calculate the distance from the start of the conveyor to the ending point.
            distance_from_start = math.sqrt((x_a - x1)**2 + (y_a - y1)**2)
            # Update the distance.
            distance = min(distance, distance_to_start + distance_from_start)

# Print the minimum time to get to the ending point.
print(distance)