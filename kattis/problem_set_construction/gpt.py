# 3.6 wrong answer 0/22
from itertools import combinations

n, k, t = map(int, input().split())

problems = []
for i in range(n):
    p, s = map(float, input().split())
    problems.append((p, s))

difficulties = []
for i in range(n):
    p_i, s_i = problems[i]
    count = 0
    total_prob = 0
    for subset in combinations(range(n-1), k-1):
        subset_prob = 1.0
        subset_time = 0
        for j in subset:
            if j >= i:
                j += 1
            subset_prob *= (1 - problems[j][0])
            subset_time += problems[j][1]
        total_prob += subset_prob * p_i
        if subset_time > t - s_i:
            count += 1
    difficulties.append(total_prob / (n-k+1-count))

for d in difficulties:
    print('{:.6f}'.format(d))
