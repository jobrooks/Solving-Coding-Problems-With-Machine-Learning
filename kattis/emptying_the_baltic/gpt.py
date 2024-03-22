# 5.5 wrong answer 0/29
from collections import deque

# read input
h, w = map(int, input().split())
altitude = [list(map(int, input().split())) for _ in range(h)]
i, j = map(int, input().split())
i -= 1
j -= 1

# initialize BFS queue
queue = deque([(i, j)])

# initialize visited set
visited = set([(i, j)])

# initialize water level
water_level = -altitude[i][j]

# perform BFS
drained_volume = 0
while queue:
    x, y = queue.popleft()
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                visited.add((nx, ny))
                if altitude[nx][ny] < altitude[x][y]:
                    queue.append((nx, ny))
                    water_level -= altitude[nx][ny]
                else:
                    drained_volume += water_level
                    water_level = max(water_level - altitude[nx][ny], 0)

# output result
print(drained_volume)
