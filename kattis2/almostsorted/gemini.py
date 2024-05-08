n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for i in range(n):
    if arr[i] == q:
        for j in range(i, n):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                break
        break

print(*arr)