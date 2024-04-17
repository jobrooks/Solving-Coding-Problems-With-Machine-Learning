from collections import deque
import sys

def main():
    n, k = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(n)]
    covered = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_covered(points[i], points[j], points[k]):
                    covered.add((i, j, k))
    #print(covered)
    queue = deque([(0, 0, 1, set())])
    visited = set()
    while queue:
        i, j, k, s = queue.popleft()
        if (i, j, k) in visited:
            continue
        visited.add((i, j, k))
        if len(s) == k:
            if len(s) not in best:
                best[len(s)] = []
            best[len(s)].append(s)
            continue
        #print(i, j, k, s)
        queue.append((i+1, j, k, s))
        queue.append((i, j+1, k, s))
        queue.append((i, j, k+1, s))
        for l in range(n):
            if l in s:
                continue
            if is_covered(points[i], points[j], points[l]):
                continue
            queue.append((i, j, k, s | {l}))
    #print(best)
    print(*best[k])

def is_covered(p1, p2, p3):
    #print(p1, p2, p3)
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) <= 0

best = {}
main()