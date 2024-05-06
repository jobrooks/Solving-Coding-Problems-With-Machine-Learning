import sys
input = sys.stdin.readline

n = int(input())
ranges = []
for _ in range(n):
    l, u = map(int, input().split())
    ranges.append((l, u))
    
ranges.sort(key=lambda x: x[0])

answer = 1
current_max = ranges[0][1]

for l, u in ranges[1:]:
    if l > current_max:
        current_max = u
        answer += 1
        
print(answer)