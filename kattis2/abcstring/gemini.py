def partition_string(s):
    """Finds the minimum number of subsequences that a string can be partitioned into,
    such that each subsequence is a beautiful string.

    Args:
        s (str): The input string.

    Returns:
        int: The minimum number of subsequences.
    """

    # Check if the string is valid.
    if len(s) % 3 != 0 or not all(c in s for c in "ABC"):
        return -1

    # Count the number of characters in the string.
    a_count = s.count("A")
    b_count = s.count("B")
    c_count = s.count("C")

    # Calculate the minimum number of subsequences.
    min_subsequences = max(a_count, b_count, c_count)

    # Return the minimum number of subsequences.
    return min_subsequences


# Get the input string.
s = input()

# Find the minimum number of subsequences.
min_subsequences = partition_string(s)

# Print the minimum number of subsequences.
print(min_subsequences)