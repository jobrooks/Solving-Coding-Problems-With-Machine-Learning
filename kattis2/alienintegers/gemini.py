def is_alien(a, b):
    sa = set(str(a))
    sb = set(str(b))
    return not bool(sa & sb)


def find_nearest_alien(n):
    if n == 1234567890:
        return "Impossible"

    # Find the smallest alien number greater than n
    greater = n + 1
    while not is_alien(n, greater):
        greater += 1

    # Find the largest alien number smaller than n
    smaller = n - 1
    while not is_alien(n, smaller):
        smaller -= 1

    # Return the nearest alien number
    if abs(n - smaller) == abs(n - greater):
        return f"{smaller} {greater}"
    elif abs(n - smaller) < abs(n - greater):
        return smaller
    else:
        return greater


if __name__ == "__main__":
    n = int(input())
    result = find_nearest_alien(n)
    print(result)