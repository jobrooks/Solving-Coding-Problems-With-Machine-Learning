import sys

inf = float('inf')

def floyd_warshall(adj, n):
    for k in range(n):
        for i in range(n):
            if adj[i][k] == inf:
                continue
            for j in range(n):
                if adj[k][j] == inf:
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

def main():
    n, m = map(int, sys.stdin.readline().split())
    inspections = list(map(int, sys.stdin.readline().split()))
    flights = [list(map(lambda x: inf if x == -1 else x, sys.stdin.readline().split())) for _ in range(n)]
    for i in range(n):
        flights[i][i] = 0
    floyd_warshall(flights, n)

    departure = {}
    for line in sys.stdin:
        s, f, t = map(int, line.split())
        s -= 1
        f -= 1
        if (s, t) not in departure:
            departure[(s, t)] = []
        departure[(s, t)].append(f)

    planes = 0
    last = {}
    for (s, t), fs in departure.items():
        if s not in last:
            last[s] = -inf
        for f in fs:
            if last[s] + inspections[s] + flights[s][f] <= t:
                last[f] = t
            else:
                planes += 1
                last[f] = t + inspections[f]

    print(planes)

if __name__ == "__main__":
    main()