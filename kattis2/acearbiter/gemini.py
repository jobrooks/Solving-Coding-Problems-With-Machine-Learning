# 5.0 Error 1/40
n = int(input())
scores = []
for i in range(n):
    scores.append(input())

for i in range(1, n):
    prev_score = scores[i - 1].split('-')
    curr_score = scores[i].split('-')
    if int(prev_score[0]) < int(curr_score[0]) - 1 or int(prev_score[1]) < int(curr_score[1]) - 1:
        print('error', i)
        break
else:
    print('ok')