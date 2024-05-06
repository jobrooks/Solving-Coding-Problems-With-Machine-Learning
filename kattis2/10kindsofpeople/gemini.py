# 4.6 Error 1/25
from collections import deque

def is_valid(grid, r, c, binary):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    if binary:
        return grid[r][c] == '0'
    else:
        return grid[r][c] == '1'

def bfs(grid, r1, c1, r2, c2, binary):
    queue = deque()
    queue.append((r1, c1))
    visited = set()
    visited.add((r1, c1))

    while queue:
        r, c = queue.popleft()
        if r == r2 and c == c2:
            return True

        if is_valid(grid, r + 1, c, binary) and (r + 1, c) not in visited:
            queue.append((r + 1, c))
            visited.add((r + 1, c))
        if is_valid(grid, r - 1, c, binary) and (r - 1, c) not in visited:
            queue.append((r - 1, c))
            visited.add((r - 1, c))
        if is_valid(grid, r, c + 1, binary) and (r, c + 1) not in visited:
            queue.append((r, c + 1))
            visited.add((r, c + 1))
        if is_valid(grid, r, c - 1, binary) and (r, c - 1) not in visited:
            queue.append((r, c - 1))
            visited.add((r, c - 1))

    return False

def main():
    r, c = map(int, input().split())
    grid = [input() for _ in range(r)]
    q = int(input())
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        if bfs(grid, r1, c1, r2, c2, True):
            print("binary")
        elif bfs(grid, r1, c1, r2, c2, False):
            print("decimal")
        else:
            print("neither")

if __name__ == "__main__":
    main()