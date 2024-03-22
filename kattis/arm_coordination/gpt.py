# 1.7 accepted 28/28

import math

# Read the input values
x, y = map(int, input().split())
r = int(input())

# Calculate the coordinates of the top-left and bottom-right corners of the square
left = x - r
right = x + r
top = y - r
bottom = y + r

# Output the coordinates of the corners
print(left, top)
print(right, top)
print(right, bottom)
print(left, bottom)
