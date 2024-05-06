from collections import defaultdict

def main():
    m, n = map(int, input().split())
    relations = defaultdict(list)
    for _ in range(m):
        a, b = input().split()
        relations[a].append(b)
    for _ in range(n):
        a, b = input().split()
        relations[a].append(b)

    # Find the transitive closure of the relations
    transitive_closure = defaultdict(list)
    for a in relations:
        visited = set()
        dfs(a, transitive_closure, visited, relations)

    # Find the number of distinct complexity classes
    distinct_classes = set()
    for a in relations:
        distinct_classes.add(a)
        for b in transitive_closure[a]:
            distinct_classes.add(b)

    # Output the minimum and maximum number of distinct complexity classes
    print(len(distinct_classes), len(distinct_classes))


def dfs(a, transitive_closure, visited, relations):
    if a in visited:
        return
    visited.add(a)
    for b in relations[a]:
        transitive_closure[a].append(b)
        dfs(b, transitive_closure, visited, relations)


if __name__ == "__main__":
    main()