def find_largest_set(m):
    """
    Finds the largest set of substances that Harry can use to create substance m.

    Args:
        m: The substance that Harry wants to create.

    Returns:
        A tuple containing the size of the set and the set of substances.
    """

    # Initialize the set of substances to the empty set.
    substances = set()

    # Iterate over the substances from 1 to m.
    for i in range(1, m + 1):
        # If the substance i is not in the set, add it to the set.
        if i not in substances:
            # Add the substance i to the set.
            substances.add(i)

            # Calculate the bitwise xor of the substances in the set.
            xor = 0
            for substance in substances:
                xor ^= substance

            # If the bitwise xor of the substances in the set is equal to m, return the set.
            if xor == m:
                return len(substances), substances

    # If no set of substances can be found to create substance m, return -1.
    return -1


def main():
    """
    Reads the input and prints the output for each test case.
    """

    # Read the number of test cases.
    t = int(input())

    # Iterate over the test cases.
    for _ in range(t):
        # Read the value of m.
        m = int(input())

        # Find the largest set of substances that Harry can use to create substance m.
        size, substances = find_largest_set(m)

        # Print the size of the set.
        print(size)

        # Print the substances in the set.
        for substance in substances:
            print(substance, end=" ")
        print()


if __name__ == "__main__":
    main()