import heapq

n, k = map(int, input().split())
jobs = []
for _ in range(n):
    t, l = map(int, input().split())
    jobs.append((t, l))

jobs.sort()

pq = []  # min-heap of job end times
cnt = 0  # number of completed jobs
ans = []  # answer for each job

for t, l in jobs:
    # remove finished jobs from the heap
    while pq and pq[0] <= t:
        heapq.heappop(pq)

    # add the current job to the heap
    heapq.heappush(pq, t + l)

    # update the answer
    ans.append(max(0, len(pq) - k))

print(*ans, sep="\n")