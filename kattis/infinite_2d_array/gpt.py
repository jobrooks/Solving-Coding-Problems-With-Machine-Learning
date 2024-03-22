# 5.2 Memory Limit Exceeded 5/106
MOD = 1000000007

x, y = map(int, input().split())

# Initialize base cases
F = [[0 for j in range(y+1)] for i in range(x+1)]
F[0][1] = F[1][0] = 1

# Calculate F[i][j] using recurrence relation
for i in range(2, x+1):
    F[i][0] = (F[i-1][0] + F[i-2][0]) % MOD
for j in range(2, y+1):
    F[0][j] = (F[0][j-1] + F[0][j-2]) % MOD
for i in range(1, x+1):
    for j in range(1, y+1):
        F[i][j] = (F[i-1][j] + F[i][j-1]) % MOD

print(F[x][y])
