import bisect
N, K = map(int, input().split())

jobs = []
for _ in range(N):
    t, l = map(int, input().split())
    jobs.append((t,l))

done = [0] * N
machines = []

for i in range(N):
    t, l = jobs[i]
    idx = bisect.bisect_left(machines, t)
    if idx < K:
        done[i] = 1
        machines[idx] = t + l
    else:
        # remove a job that ends first
        machines[idx - K] = t + l

ans = []
for i in range(N):
    ans.append(max(K, sum(done[:i+1])) - sum(done[:i+1]))

for x in ans:
    print(x)