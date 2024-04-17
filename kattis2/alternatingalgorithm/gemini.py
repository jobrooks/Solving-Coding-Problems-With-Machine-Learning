n = int(input())
a = list(map(int, input().split()))

rounds = 0
while True:
    swapped = False
    for i in range(0, n, 2):
        if i + 1 < n and a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True
    if swapped:
        rounds += 1
    else:
        break

print(rounds)