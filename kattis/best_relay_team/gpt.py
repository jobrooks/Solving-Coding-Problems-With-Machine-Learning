# 1.8 time limit exceeded 4/27

n = int(input())
runners = []
for i in range(n):
    name, a, b = input().split()
    a = float(a)
    b = float(b)
    runners.append((name, a, b))

best_time = float('inf')
best_team = []

# Try all possible combinations of runners for the four legs
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if k == i or k == j:
                continue
            for l in range(n):
                if l == i or l == j or l == k:
                    continue

                # Calculate the total time for this team
                time = runners[i][1] + runners[j][2] + runners[k][2] + runners[l][2]
                if time < best_time:
                    best_time = time
                    best_team = [runners[i][0], runners[j][0], runners[k][0], runners[l][0]]

# Output the result
print('{:.2f}'.format(best_time))
print(best_team[0])
print(best_team[1])
print(best_team[2])
print(best_team[3])
