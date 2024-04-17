import sys

def count_patterns(N, d, s, t, f_min, f_max, L):
    """Counts the number of lacing patterns that meet the given requirements.

    Args:
        N: The number of eyelets on a side.
        d: The distance between eyelets.
        s: The separation between the columns of eyelets.
        t: The thickness of an eyelet.
        f_min: The minimum free end length.
        f_max: The maximum free end length.
        L: The length of the shoelace.

    Returns:
        The number of lacing patterns that meet the given requirements.
    """

    # Check if the input is valid.

    if not (2 <= N <= 9 and 5 <= d <= 30 and 10 <= s <= 50 and 0 <= t <= 4 and 0 <= f_min <= f_max <= 2000 and 200 <= L <= 2000):
        raise ValueError("Invalid input.")

    # Compute the total length of the shoelace that is used for lacing.

    total_length = 2 * L - f_min - f_max

    # Compute the number of eyelets that the shoelace must pass through.

    num_eyelets = total_length // (d + s + 2 * t)

    # If the number of eyelets is not even, then the shoelace cannot be laced.

    if num_eyelets % 2 != 0:
        return 0

    # Compute the number of ways to lace the shoelace.

    num_patterns = 0
    for i in range(num_eyelets // 2, num_eyelets + 1):
        num_patterns += binomial(num_eyelets, i) * binomial(i, i // 2)

    # Return the number of lacing patterns that meet the given requirements.

    return num_patterns


def binomial(n, k):
    """Computes the binomial coefficient.

    Args:
        n: The number of items.
        k: The number of items to choose.

    Returns:
        The binomial coefficient.
    """

    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)


def main():
    """Gets the input and prints the number of lacing patterns for each shoelace length."""

    # Get the input.

    N, d, s, t, f_min, f_max = map(int, sys.stdin.readline().split())
    L = list(map(int, sys.stdin.readlines()))

    # Compute the number of lacing patterns for each shoelace length.

    num_patterns = [count_patterns(N, d, s, t, f_min, f_max, L[i]) for i in range(len(L))]

    # Print the number of lacing patterns for each shoelace length.

    print(" ".join(map(str, num_patterns)))


if __name__ == "__main__":
    main()