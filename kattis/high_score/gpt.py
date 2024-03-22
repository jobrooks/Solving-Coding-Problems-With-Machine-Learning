# 5.7 wrong answer 29/30
n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    # calculate the score for all possible distributions of wildcard tokens
    scores = [a*a + b*b + c*c + 7*min(a, b, c)]
    if d > 0:
        for j in range(3):
            if j == 0:
                temp = (a + d, b, c)
            elif j == 1:
                temp = (a, b + d, c)
            else:
                temp = (a, b, c + d)
            scores.append(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2] + 7*min(temp))
    # output the maximum score
    print(max(scores))
