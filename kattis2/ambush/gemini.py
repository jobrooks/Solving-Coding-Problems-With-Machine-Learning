L, A, B, P = map(int, input().split())

if (A <= P <= B) or (B <= P <= A):
    print(0)
else:
    print(1)