# 5.5 wrong answer 0/8
import itertools

def find_order(n, names, dislikes):
    graph = {name: set() for name in names}
    for a, b in dislikes:
        graph[a].add(b)
        graph[b].add(a)

    def backtrack(path):
        if len(path) == n:
            return path
        last_node = path[-1]
        for node in graph[last_node] | {name for name in names if name not in path}:
            if node not in path and all(d not in path for d in graph[node]):
                solution = backtrack(path + [node])
                if solution is not None:
                    return solution

    solution = backtrack([next(iter(graph))])
    if solution is None:
        return "You all need therapy."
    return " ".join(solution)

while True:
    try:
        n = int(input())
    except EOFError:
        break
    names = [input().strip() for _ in range(n)]
    m = int(input())
    dislikes = [input().split() for _ in range(m)]
    print(find_order(n, names, dislikes))
