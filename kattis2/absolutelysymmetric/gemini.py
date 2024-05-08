# 4.0 Error 1/36
from collections import deque
from typing import List

def main():
    n = int(input())
    a = [[int(x) for x in input().split()] for _ in range(n)]

    # Check if the matrix is absolutely symmetric
    for i in range(n):
        for j in range(n):
            if abs(a[i][j]) != abs(a[j][i]):
                print(-1)
                return

    # Decompose the matrix into a sum of absolutely symmetric matrices
    x = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(a, 0)])
    while q:
        a, k = q.popleft()
        if k == n:
            continue
        for i in range(n):
            for j in range(n):
                if abs(a[i][j]) != abs(a[j][i]):
                    x[i][j] += a[i][j]
                    a[i][j] = -a[i][j]
                    q.append((a, k + 1))
                    x[i][j] -= a[i][j]
                    a[i][j] = -a[i][j]

    # Print the decomposed matrices
    print(k)
    for i in range(k):
        for j in range(n):
            for l in range(n):
                print(x[j][l], end=' ')
            print()

if __name__ == "__main__":
    main()