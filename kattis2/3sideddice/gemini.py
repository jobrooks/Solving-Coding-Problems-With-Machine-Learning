def is_feasible(dice, target):
    """
    Check if it is possible to simulate the target die using the given dice.

    Parameters:
        dice: A list of 3 lists, each representing a die with 3 possible outcomes.
        target: A list representing the target die with 3 possible outcomes.

    Returns:
        True if it is possible to simulate the target die, False otherwise.
    """

    # Check if the probabilities of the target die add up to 10000.
    if sum(target) != 10000:
        return False

    # Check if there is a die that can produce each outcome of the target die.
    for i in range(3):
        if max(dice[i]) >= target[i]:
            return True

    return False


def main():
    # Read the input.
    test_cases = []
    while True:
        line = input()
        if line == "0 0 0":
            break
        test_cases.append([list(map(int, input().split())) for _ in range(4)])

    # Process each test case.
    for test_case in test_cases:
        dice = test_case[:-1]
        target = test_case[-1]
        if is_feasible(dice, target):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()