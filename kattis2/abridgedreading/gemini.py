from collections import defaultdict, deque

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    pages = list(map(int, f.readline().split()))
    dependencies = defaultdict(list)
    for _ in range(m):
        a, b = map(int, f.readline().split())
        dependencies[a].append(b)

# Find the Culminating Concept chapters
culminating_concepts = []
for i in range(1, n + 1):
    if not dependencies[i]:
        culminating_concepts.append(i)

# Find the shortest path to each Culminating Concept chapter
dist = defaultdict(lambda: float('inf'))
dist[1] = 0
q = deque([1])
while q:
    curr = q.popleft()
    for next in dependencies[curr]:
        if dist[next] > dist[curr] + pages[next - 1]:
            dist[next] = dist[curr] + pages[next - 1]
            q.append(next)

# Find the two Culminating Concept chapters with the shortest path
min_paths = sorted(dist[culminating_concepts])[:2]

# Output the minimum number of pages that need to be read
print(sum(min_paths))