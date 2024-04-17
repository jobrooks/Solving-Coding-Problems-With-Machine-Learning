def find_degree_and_next_value(input_values):
    """
    Finds the degree of a minimal-degree polynomial that produces the given sequence and the value of the polynomial
    if evaluated at the next regularly spaced input value.

    Parameters:
        input_values: A list of integers representing the values of a polynomial when evaluated at n regularly spaced
            input values.

    Returns:
        A tuple containing two integers: the degree of the minimal-degree polynomial and the value of the polynomial if
        evaluated at the next regularly spaced input value.
    """

    # Check if the input is valid.
    if len(input_values) < 2 or len(input_values) > 10:
        raise ValueError("Invalid input: the number of polynomial evaluations must be between 2 and 10.")

    for v in input_values:
        if v < -2000000 or v > 2000000:
            raise ValueError(f"Invalid input: the value {v} is not in the range [-2,000,000, 2,000,000].")

    # Find the differences between consecutive values in the sequence.
    differences = [input_values[i + 1] - input_values[i] for i in range(len(input_values) - 1)]

    # Find the degree of the minimal-degree polynomial.
    degree = 0
    while differences:
        # Find the differences between consecutive values in the differences.
        differences = [differences[i + 1] - differences[i] for i in range(len(differences) - 1)]
        degree += 1

    # Find the value of the polynomial if evaluated at the next regularly spaced input value.
    next_value = input_values[-1] + differences[-1]

    return degree, next_value


def main():
    # Get the input.
    n = int(input())
    input_values = [int(x) for x in input().split()]

    # Find the degree of the minimal-degree polynomial and the value of the polynomial if evaluated at the next
    # regularly spaced input value.
    degree, next_value = find_degree_and_next_value(input_values)

    # Print the output.
    print(f"{degree} {next_value}")


if __name__ == "__main__":
    main()