from collections import defaultdict

n = int(input())
roads = defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

visited = set()
for city in roads:
    if city not in visited:
        visited.add(city)
        stack = [city]
        while stack:
            current = stack.pop()
            for neighbor in roads[current]:
                if neighbor not in visited:
                    print(current, neighbor)
                    visited.add(neighbor)
                    stack.append(neighbor)