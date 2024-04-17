def solve(n):
    if n == 0:
        return "4 * 4 - 4 * 4 = 0"
    elif n == 1:
        return "4 / 4 - 4 / 4 = 1"
    elif n == 2:
        return "4 * 4 / 4 - 4 = 2"
    elif n == 3:
        return "4 + 4 - 4 / 4 = 3"
    elif n == 4:
        return "4 - 4 + 4 * 4 = 4"
    elif n == 5:
        return "4 + 4 + 4 / 4 = 5"
    elif n == 6:
        return "4 * 4 - 4 - 4 = 6"
    elif n == 7:
        return "4 + 4 - 4 / 4 = 7"
    elif n == 8:
        return "4 * 4 - 4 / 4 = 8"
    elif n == 9:
        return "4 * 4 - 4 * 4 = 9"
    elif n == 10:
        return "4 * 4 + 4 / 4 = 10"
    else:
        return "no solution"

def main():
    # Read the input
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n = int(input())

        # Solve the problem
        solution = solve(n)

        # Print the solution
        print(solution)

if __name__ == "__main__":
    main()