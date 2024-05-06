# 5.7 wrong answer 1/32
from collections import defaultdict, deque

def main():
    n, m = map(int, input().split())
    pages = list(map(int, input().split()))
    deps = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        deps[a].append(b)

    # Perform topological sort
    in_degree = [0] * (n + 1)
    for node in deps:
        for neighbor in deps[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in range(1, n + 1) if in_degree[node] == 0])
    num_pages = 0
    cc_count = 0
    while queue:
        node = queue.popleft()
        num_pages += pages[node - 1]
        if in_degree[node] == 0:
            cc_count += 1
        for neighbor in deps[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        if cc_count == 2:
            break

    print(num_pages)

if __name__ == "__main__":
    main()