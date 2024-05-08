from collections import defaultdict

n, m, k, t = map(int, input().split())

statements = defaultdict(list)
for _ in range(m):
    a, b, s = input().split()
    statements[a].append((b, s))

identities = {}
for statement in statements[str(k)]:
    b, s = statement
    if s == "imposter":
        identities[b] = "imposter"
    else:
        identities[b] = "crewmate"

if len(identities) == 0:
    print(-1)
else:
    earliest_statement = min(map(int, identities.keys()))
    print(earliest_statement if earliest_statement <= m - t else -1)