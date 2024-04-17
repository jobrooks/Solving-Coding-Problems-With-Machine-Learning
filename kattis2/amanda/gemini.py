import sys

def main():
  n, m = map(int, sys.stdin.readline().split())
  edges = [[]] * (n+1)
  for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
  lounges = set()
  for i in range(1, n+1):
    if not lounges:
      lounges.add(i)
    else:
      found = False
      for j, c in edges[i]:
        if j in lounges and c == 2:
          found = True
          break
      if not found:
        lounges.add(i)
  if len(lounges) == n:
    print('impossible')
  else:
    print(len(lounges))

if __name__ == '__main__':
  main()