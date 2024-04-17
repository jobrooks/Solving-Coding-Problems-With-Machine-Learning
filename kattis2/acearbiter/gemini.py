n = int(input())
score = [(0, 0)]
for i in range(n):
    a, b = map(int, input().split('-'))
    if a>11 or b>11 or (a+b)%2==0 or (a==11 and b==11) or a==b:
        print('error', i+1)
        exit(0)
    score.append((a, b))
score.sort()
for i in range(1, len(score)):
    if score[i][0]<score[i-1][0] or score[i][1]<score[i-1][1]:
        print('error', i)
        exit(0)
print('ok')