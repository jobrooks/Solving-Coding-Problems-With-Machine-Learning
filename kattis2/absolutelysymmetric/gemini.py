import numpy as np

n = int(input())
A = np.array([[int(x) for x in input().split()] for _ in range(n)])

if np.abs(A).tolist() == np.abs(A.T).tolist():
    k = 1
    X1 = np.abs(A)
else:
    k = 2
    X1 = np.abs(A[:, ::2]) - np.abs(A[:, 1::2])
    X2 = np.abs(A[:, 1::2]) + np.abs(A[:, ::2])

print(k)
for X in [X1, X2]:
    for x in X.tolist():
        print(*x)