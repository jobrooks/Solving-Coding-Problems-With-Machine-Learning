# 2.3 accepted 7/7

n, m = map(int, input().split())
groups = list(map(int, input().split()))

rejected = 0
seats_left = n

for group_size in groups:
    if group_size > seats_left:
        rejected += 1
    else:
        seats_left -= group_size

print(rejected)
