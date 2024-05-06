def is_alien(a, b):
    str_a = list(str(a))
    str_b = list(str(b))
    for digit in str_a:
        if digit in str_b:
            return False
    return True


def find_nearest_alien(n):
    # Check if n is alien to 1234567890
    if is_alien(n, 1234567890):
        return n

    # Find the smallest alien number greater than n
    greater = n + 1
    while not is_alien(greater, n):
        greater += 1

    # Find the largest alien number smaller than n
    smaller = n - 1
    while not is_alien(smaller, n):
        smaller -= 1

    # Return the nearest alien number
    if greater - n < n - smaller:
        return greater
    elif greater - n > n - smaller:
        return smaller
    else:
        return [smaller, greater]  # Return both if they are equally close


if __name__ == "__main__":
    n = int(input())  # Read the input number
    result = find_nearest_alien(n)

    if isinstance(result, list):
        print(*result)  # Print the two alien numbers if they exist
    elif result:
        print(result)  # Print the single alien number if it exists
    else:
        print("Impossible")  # Print "Impossible" if no alien number exists