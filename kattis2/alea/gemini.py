def roll(A, C, X, n):
    X = ((A * X + C) % 2 ** 32)
    return 1 + ((X >> 16) % 6)

def play(A, C, X):
    used = [0 for i in range(12)]
    rolls = [0 for i in range(11)]
    score = 0
    for i in range(11):
        for j in range(3):
            rolls[i] = roll(A, C, X, i * 3 + j)
        rolls[i].sort()
        fiv = rolls[i].count(rolls[i][0])
        fou = rolls[i].count(rolls[i][1])
        thr = rolls[i].count(rolls[i][2])
        two = rolls[i].count(rolls[i][3])
        one = rolls[i].count(rolls[i][4])
        if fiv == 5:
            if used[8]:
                score += 0
            else:
                used[8] = 1
                score += 50
        elif fiv == 4 and one == 1:
            if used[7]:
                score += 0
            else:
                used[7] = 1
                score += 21
        elif thr == 3 and two == 2:
            if used[6]:
                score += 0
            else:
                used[6] = 1
                score += 20
        elif two == 4 and one == 1:
            if used[5]:
                score += 0
            else:
                used[5] = 1
                score += 19
        elif thr == 3 and one == 2:
            if used[4]:
                score += 0
            else:
                used[4] = 1
                score += 18
        elif two == 3 and one == 1:
            if used[3]:
                score += 0
            else:
                used[3] = 1
                score += 17
        elif fiv == 3 and two == 1:
            if used[2]:
                score += 0
            else:
                used[2] = 1
                score += 16
        elif fou == 3 and one == 2:
            if used[1]:
                score += 0
            else:
                used[1] = 1
                score += 15
        elif fou == 2 and two == 2:
            if used[0]:
                score += 0
            else:
                used[0] = 1
                score += 14
        elif fiv == 4:
            if used[11]:
                score += 0
            else:
                used[11] = 1
                score += 13
        elif fiv == 2 and thr == 3:
            if used[10]:
                score += 0
            else:
                used[10] = 1
                score += 12
        elif fou == 4:
            if used[9]:
                score += 0
            else:
                used[9] = 1
                score += 11
        else:
            score += sum(rolls[i])
    return score

while True:
    A, C, X = map(int, input().split())
    if A == C == X == 0:
        break
    print(play(A, C, X))