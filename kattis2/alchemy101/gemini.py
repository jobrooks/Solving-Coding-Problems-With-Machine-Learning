import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    ans = []
    for i in range(1, m+1):
        if (1<<i) & m:
            ans.append(i)
    print(len(ans))
    print(*ans)