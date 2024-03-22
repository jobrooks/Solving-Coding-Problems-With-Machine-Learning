# 4.6 wrong answer 0/15
def update(bit, i, v):
    while i < len(bit):
        bit[i] += v
        i += i & -i

def query(bit, i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i & -i
    return res

n, m = map(int, input().split())
scores = [(0, 0)] * (n + 1)
for i in range(1, n + 1):
    scores[i] = (0, i)  # initialize with zero solved problems and team number
bit = [0] * (n + 1)
rank = 1
for i in range(m):
    t, p = map(int, input().split())
    a, b = scores[t]
    update(bit, t, -b)  # remove the old penalty
    b += p
    a += (p == 1)  # increment solved problems if penalty is 1
    scores[t] = (a, b)
    update(bit, t, b)  # add the new penalty
    r = query(bit, n) - query(bit, 1) + 1  # calculate rank
    if t == 1:
        rank = r
    print(rank)
