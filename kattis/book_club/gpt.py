# 5.2 wrong answer 0/16
def find_cycles(n, adj_list):
    # Step 1: Run DFS to compute finish times
    visited = [False] * n
    finish_times = []
    for i in range(n):
        if not visited[i]:
            dfs_visit(i, visited, adj_list, finish_times)

    # Step 2: Reverse the graph
    rev_adj_list = [[] for _ in range(n)]
    for i in range(n):
        for j in adj_list[i]:
            rev_adj_list[j].append(i)

    # Step 3: Run DFS in reverse order of finish times to compute SCCs
    visited = [False] * n
    sccs = []
    for i in reversed(finish_times):
        if not visited[i]:
            scc = []
            dfs_visit(i, visited, rev_adj_list, scc)
            sccs.append(scc)

    # Step 4: Check if there is an SCC that contains all nodes
    for scc in sccs:
        if len(scc) == n:
            return True

    return False


def dfs_visit(node, visited, adj_list, finish_times):
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs_visit(neighbor, visited, adj_list, finish_times)
    finish_times.append(node)


# Read input
n, m = map(int, input().split())
adj_list = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)

# Find cycles that cover all nodes
if find_cycles(n, adj_list):
    print("YES")
else:
    print("NO")
