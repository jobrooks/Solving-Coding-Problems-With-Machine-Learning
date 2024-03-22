# 5.8 wrong answer 1/60
n = int(input())
cheetahs = []
for i in range(n):
    t, v = map(int, input().split())
    cheetahs.append((t, v))

cheetahs.sort()  # sort cheetahs by start time

first_pos = 0
last_pos = sum(v * (t2 - t1) for (t1, v), (t2, _) in zip(cheetahs, cheetahs[1:]))  # initialize last_pos

min_dist = last_pos  # initialize min_dist to the distance at the end of the simulation

for t, v in cheetahs:
    last_pos -= v * (t - cheetahs[0][0])  # update last_pos
    min_dist = min(min_dist, last_pos - first_pos)  # update min_dist
    first_pos += v * (t - cheetahs[0][0])  # update first_pos

print("{:.3f}".format(min_dist))
