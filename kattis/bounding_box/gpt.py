# 3.6 run-time error 0/5

import math

EPS = 1e-9

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def area(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

while True:
    n = int(input())
    if n == 0:
        break
    
    x1, y1, x2, y2, x3, y3 = map(float, input().split())
    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)
    
    for i in range(3, n):
        x, y = map(float, input().split())
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    # check if any of the vertices lie on the bounding box
    if x1 == min_x or x1 == max_x or y1 == min_y or y1 == max_y:
        print("0.000")
    elif x2 == min_x or x2 == max_x or y2 == min_y or y2 == max_y:
        print("0.000")
    elif x3 == min_x or x3 == max_x or y3 == min_y or y3 == max_y:
        print("0.000")
    else:
        # calculate area of triangle formed by the vertices
        tri_area = area(x1, y1, x2, y2, x3, y3)
        # calculate area of bounding box
        box_area = (max_x - min_x) * (max_y - min_y)
        # output the difference between the two areas
        print("%.3f" % (box_area - tri_area + EPS))
