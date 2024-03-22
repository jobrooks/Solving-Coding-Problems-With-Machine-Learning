# 5.3 Wrong Answer 0/50
r, c = map(int, input().split())
grid = [input().rstrip() for _ in range(2*r-1)]

triangles = 0
for i in range(1, 2*r-1, 2):
    for j in range(1, 2*c-1, 2):
        if grid[i][j] != 'x':
            continue
        if i > 1 and j > 1 and grid[i-2][j-2] == '-' and grid[i-1][j-1] == '\\' and grid[i][j-2] == '/' and grid[i-1][j-3] == '-':
            triangles += 1
        if i > 1 and j < 2*c-2 and grid[i-2][j+2] == '-' and grid[i-1][j+1] == '/' and grid[i][j+2] == '\\' and grid[i-1][j+3] == '-':
            triangles += 1
        if i < 2*r-2 and j > 1 and grid[i+2][j-2] == '-' and grid[i+1][j-1] == '/' and grid[i][j-2] == '\\' and grid[i+1][j-3] == '-':
            triangles += 1
        if i < 2*r-2 and j < 2*c-2 and grid[i+2][j+2] == '-' and grid[i+1][j+1] == '\\' and grid[i][j+2] == '/' and grid[i+1][j+3] == '-':
            triangles += 1

print(triangles)
