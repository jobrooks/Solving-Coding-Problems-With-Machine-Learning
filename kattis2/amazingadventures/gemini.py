from collections import deque

def bfs(grid, start, end):
    queue = deque([(start, "")])
    while queue:
        (row, col), path = queue.popleft()
        if (row, col) == end:
            return path
        for (dr, dc) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 'X' and (nr, nc) not in path:
                queue.append(((nr, nc), path + "RLDU"[dr + dc]))
    return None

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [['.'] * m for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    ban = tuple(map(int, input().split()))
    grid[end[0] - 1][end[1] - 1] = 'G'
    grid[start[0] - 1][start[1] - 1] = 'B'
    grid[ban[0] - 1][ban[1] - 1] = 'X'
    path = bfs(grid, start, end)
    if path is None:
        print("NO")
    else:
        print("YES")
        print(path)