import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
edge = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

mod = 1000000009
 
dp = [[[[0 for j in range(11)] for k in range(4)] for l in range(3)] for _ in range(N + 1)]

def dfs(now: int, par: int, cnt: int, same: int) -> int:
    ret = dp[now][par][cnt][same]
    if ret != -1:
        return ret
    
    ret = 1
    for nxt in edge[now]:
        if nxt == par:
            continue
        for sn in range(same + 1):
            for cc in range(cnt):
                ret *= dfs(nxt, now, cc + (same == sn), sn)
                ret %= mod
    dp[now][par][cnt][same] = ret
    return ret

for i in range(1,N+1):
    print(dfs(i,i,0,0), end= " ")