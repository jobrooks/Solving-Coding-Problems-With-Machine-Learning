# 4.5 runtime error 0/13
n = int(input())
a = [int(input()) for _ in range(n)]

pos = {a[i]: i for i in range(n)}  # position of each number in initial array
l, r = 0, n-1  # pointers to first and last unsorted positions
swaps = [0] * n  # number of swaps in each phase

for phase in range(n):
    if phase % 2 == 0:  # even phase, move largest number to its final position
        num = max(range(l, r+1), key=lambda i: a[i])
    else:  # odd phase, move smallest number to its final position
        num = min(range(l, r+1), key=lambda i: a[i])
    num_pos = pos[a[num]]  # position of number to move
    while num_pos != l+phase:
        # swap number with previous element
        a[num_pos], a[num_pos-1] = a[num_pos-1], a[num_pos]
        pos[a[num_pos]] = num_pos
        pos[a[num_pos-1]] = num_pos-1
        swaps[phase] += 1
        num_pos -= 1
    if num == l:
        l += 1
    elif num == r:
        r -= 1

for s in swaps:
    print(s)
