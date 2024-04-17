import sys
input = sys.stdin.readline

L, A, B, P = map(int, input().split())

if P >= A and P <= B:
    print(0)
elif P < A:
    print(A - P)
else:
    print(P - B)