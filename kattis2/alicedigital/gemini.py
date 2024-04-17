def max_weight_subarray_with_one_min(arr, n, m):
    """
    Finds the maximum weight subarray of the given array that contains only one m as the minimum element.

    Parameters:
    arr: The input array.
    n: The size of the array.
    m: The minimum element.

    Returns:
    The maximum weight subarray.
    """

    # Initialize the maximum weight and the current weight.
    max_weight = -1
    cur_weight = 0

    # Initialize the left and right pointers.
    left = 0
    right = 0

    # Iterate over the array.
    while right < n:
        # Add the current element to the current weight.
        cur_weight += arr[right]

        # If the current element is less than m, then reset the current weight and the left pointer.
        if arr[right] < m:
            cur_weight = 0
            left = right + 1

        # Update the maximum weight.
        if cur_weight > max_weight:
            max_weight = cur_weight

        # Increment the right pointer.
        right += 1

    # Return the maximum weight.
    return max_weight


# Read the number of datasets.
t = int(input())

# Iterate over the datasets.
for _ in range(t):
    # Read the size of the array and the minimum element.
    n, m = map(int, input().split())

    # Read the array.
    arr = list(map(int, input().split()))

    # Find the maximum weight subarray.
    max_weight = max_weight_subarray_with_one_min(arr, n, m)

    # Print the maximum weight.
    print(max_weight)