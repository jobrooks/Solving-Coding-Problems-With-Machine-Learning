from collections import deque
import sys

N, T = map(int, input().split())
cheers = []
for _ in range(N):
    S, D = map(int, input().split())
    cheers.append((S, D))

cheers.sort(key=lambda x: x[1])

q = deque()
q.append((0, 0, []))

min_diff = float('inf')
min_seq = []

while q:
    enthusiasm, difficulty, seq = q.popleft()

    if enthusiasm == T:
        if difficulty < min_diff:
            min_diff = difficulty
            min_seq = seq
        continue

    for i in range(N + 1):
        new_enthusiasm = enthusiasm + cheers[i - 1][0]
        if new_enthusiasm < 0 or new_enthusiasm > T:
            continue
        new_difficulty = difficulty + cheers[i - 1][1]
        new_seq = seq.copy()
        new_seq.append(i)
        q.append((new_enthusiasm, new_difficulty, new_seq))

print(len(min_seq))
print(*min_seq)