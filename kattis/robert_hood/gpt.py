# 4.7 time limit exception 3/12
import math

n = int(input())  # number of shots

# read the coordinates of the arrows
arrows = []
for i in range(n):
    x, y = map(int, input().split())
    arrows.append((x, y))

# find the maximum distance between any pair of arrows
max_distance = 0.0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = arrows[i]
        x2, y2 = arrows[j]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_distance = max(max_distance, distance)

print("{:.6f}".format(max_distance))
