n = int(input())
arr = [int(x) for x in input().split()]

# Check if the array is already sorted
is_sorted = True
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print(0)  # Already sorted, no rounds needed
else:
    # Count the number of rounds needed
    rounds = 1
    while not is_sorted:
        # Odd rounds
        for i in range(0, n, 2):
            if i + 1 < n and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # Check if the array is sorted after the odd rounds
        is_sorted = True
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                is_sorted = False
                break

        rounds += 1

        if is_sorted:
            break

        # Even rounds
        for i in range(1, n, 2):
            if i + 1 < n and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # Check if the array is sorted after the even rounds
        is_sorted = True
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                is_sorted = False
                break

        rounds += 1

    print(rounds)