# 5.7 Error 1/32
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    pages = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    culminating = []
    for i in range(1, n + 1):
        if not graph[i]:
            culminating.append(i)
    culminating.sort(key=lambda x: sum(pages[y - 1] for y in graph[x]))
    print(sum(pages[y - 1] for y in graph[culminating[0]]) + pages[culminating[0] - 1] +
          sum(pages[y - 1] for y in graph[culminating[1]]) + pages[culminating[1] - 1])