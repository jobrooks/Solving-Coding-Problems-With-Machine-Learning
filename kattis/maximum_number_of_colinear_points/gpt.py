# 4.9 Wrong Answer 0/2
while True:
    n = int(input())
    if n == 0:
        break
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    max_collinear = 0
    for i in range(n):
        for j in range(i + 1, n):
            collinear = 2
            for k in range(j + 1, n):
                if (points[i][1] - points[j][1]) * (points[i][0] - points[k][0]) == \
                   (points[i][1] - points[k][1]) * (points[i][0] - points[j][0]):
                    collinear += 1
            max_collinear = max(max_collinear, collinear)
    print(max_collinear)
