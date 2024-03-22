# 2.4 wrong answer 0/13

import math

# Read the input point
x, y = map(int, input().split())

# Find the length of the line segment
length = math.sqrt(x**2 + y**2)

# Find the angle between the line segment and the x-axis
theta = math.atan2(y, x)

# Find the coordinates of the other endpoint
# by rotating the original point by 90 degrees
# and scaling the resulting vector by the length
dx = length * math.cos(theta + math.pi/4)
dy = length * math.sin(theta + math.pi/4)

# Round the coordinates to two decimal digits
dx = round(dx, 2)
dy = round(dy, 2)

# Print the result
print(dx, dy)
