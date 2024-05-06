prev = input()
n = int(input())
names = [input() for i in range(n)]
for i in range(n):
    if names[i][0] == prev[-1]:
        print(names[i] + '!')
        break
else:
    print('?')