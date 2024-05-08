N, Q = map(int, input().split())

boxes = [0] * (N + 1)
for _ in range(Q):
    t, *x = map(int, input().split())
    if t == 1:
        l, r, a, b = x
        for i in range(l, r + 1):
            boxes[i] = (i - l + 1) * a % b
    else:
        l, r = x
        print(sum(boxes[l:r + 1]))