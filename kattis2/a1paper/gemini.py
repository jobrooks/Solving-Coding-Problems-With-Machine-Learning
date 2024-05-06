# 4.2 Error 1/13
import math

def main():
    # Read the input
    n = int(input())
    papers = [int(x) for x in input().split()]

    # Check if there are enough papers to make an A1 paper
    total_area = 0
    for i in range(n - 1):
        total_area += papers[i] * (2 ** (-3 / 4 - i * 1 / 4)) ** 2

    if total_area < 1:
        print("impossible")
        return

    # Compute the minimum amount of tape needed
    tape_length = 0
    for i in range(n - 2, -1, -1):
        if papers[i] > 0:
            tape_length += papers[i] * (2 ** (-3 / 4 - i * 1 / 4))

    # Print the output
    print(tape_length)

if __name__ == "__main__":
    main()