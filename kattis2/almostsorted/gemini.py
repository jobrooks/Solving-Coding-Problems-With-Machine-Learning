def cycle_sort(arr, n, q):
    """
    Performs cycle sort on the array and returns the state when the element q is first sorted.

    Parameters:
        arr: The array to be sorted.
        n: The length of the array.
        q: The element to find the state of.

    Returns:
        The state of the array when the element q is first sorted.
    """
    writes = 0  # Number of writes performed so far.
    for i in range(n):
        curr = arr[i]
        pos = i  # Position of the element that should be in index i.

        for j in range(i + 1, n):
            if arr[j] < curr:
                pos += 1

        if pos == i:
            continue

        while curr == arr[pos]:
            pos += 1

        arr[i], arr[pos] = arr[pos], arr[i]
        writes += 1

        if arr[pos] == q:
            return writes, list(arr)

    return writes, list(arr)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())

    writes, state = cycle_sort(arr, n, q)
    print(*state)