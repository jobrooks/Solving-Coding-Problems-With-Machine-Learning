Nmax = 13
Tmax = 999

def main():
  N, p = map(int, input().split())
  D = list(map(int, input().split()))

  MinTime = [[0] * (1<<N) for _ in range(N)]
  MinTime[0][1<<p] = D[p]

  for k in range(1, 1<<N):
    if (k & (k+1)) != 0 or (k>>p)&1 == 0: continue
    for i in range(N):
      if i == p or (k>>(i))&1 == 0: continue
      for j in range(N):
        if i == j or (k>>(j))&1 == 0: continue
        MinTime[i][k|(1<<i)] = min(MinTime[i][k|(1<<i)],
          MinTime[j][k] + D[i])

  ansTime = 1<<31
  ansNum = 0
  for i in range(N):
    if MinTime[i][(1<<N)-1] <= Tmax:
      if MinTime[i][(1<<N)-1] < ansTime:
        ansTime = MinTime[i][(1<<N)-1]
        ansNum = i

  print(ansNum, ansTime)

main()