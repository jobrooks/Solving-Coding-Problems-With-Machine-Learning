# 1.4 accepted 7/7

# read in the coordinates of the first three points
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# check which of the three points has the same x-coordinate as another point
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

# check which of the three points has the same y-coordinate as another point
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

# output the coordinates of the fourth point
print(x4, y4)
