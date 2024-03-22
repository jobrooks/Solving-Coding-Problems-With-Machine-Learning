# 3.7 accepted 8/8
n, m = map(int, input().split())
can_sizes = sorted([int(input()) for i in range(n)])
colors = [int(input()) for i in range(m)]

waste = 0
for color in colors:
    i = 0
    while can_sizes[i] < color:
        i += 1
    waste += can_sizes[i] - color

print(waste)
