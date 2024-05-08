n = int(input())
arr = list(map(int, input().split()))

is_almost_sorted = True

for i in range(1, n):
    if arr[i] < arr[i - 1]:
        is_almost_sorted = False
        break

if is_almost_sorted:
    print("Yes")
else:
    print("No")