from sys import stdin, stdout

n, q = map(int, stdin.readline().split())

stones = [0] * n

for _ in range(q):
    query = stdin.readline().split()
    if query[0] == '1':
        l, r, a, b = map(int, query[1:])
        for i in range(l-1, r):
            stones[i] = (stones[i] + ((i-l+1)*a) % b) % b
    else:
        l, r = map(int, query[1:])
        cnt = 0
        for i in range(l-1, r):
            cnt += stones[i]
        stdout.write(str(cnt) + '\n')