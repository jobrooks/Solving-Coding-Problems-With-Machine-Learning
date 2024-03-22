# 5.4 run-time error 0/27

r, c = map(int, input().split())

vertices = []
for i in range(2*r-1):
    if i % 2 == 0:
        vertices.append(input()[::4])
    else:
        input()  # skip diagonal edges

num_triangles = 0
for i in range(r):
    for j in range(c):
        if vertices[i][j] == 'x':
            for dx, dy in ((0, 1), (1, 0), (1, 1), (1, -1)):
                x1, y1 = i+dx, j+dy
                x2, y2 = x1+dx, y1+dy
                if 0 <= x2 < r and 0 <= y2 < c and \
                        vertices[x1][y1] == vertices[x2][y2] == 'x':
                    num_triangles += 1

print(num_triangles)