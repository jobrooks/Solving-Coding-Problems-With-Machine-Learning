import sys
input = sys.stdin.readline
computers, existing_cables = map(int,input().split())
existing = [[] for i in range(computers)]
for i in range(existing_cables):
    a,b = map(int,input().split())
    existing[a].append(b)
    existing[b].append(a)
for i in range(computers):
    existing[i].sort()
components = 0
cnt = 0
vis = [0]*computers
for i in range(computers):
    if vis[i]==0:
        components+=1
        cnt+=dfs(i,vis,existing)
def dfs(node,vis,existing):
    vis[node]=1
    c = 1
    for u in existing[node]:
        if vis[u]==0:
            c=max(c,1+dfs(u,vis,existing))
    return c
print(components+cnt-1)