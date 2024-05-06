# 4.2 wrong answer 1/13
import math

def main():
    n = int(input())
    sheets = list(map(int, input().split()))

    # Calculate the area of an A1 paper
    a1_width = 2 ** (-5/4)
    a1_height = 2 ** (-3/4)
    a1_area = a1_width * a1_height

    # Calculate the area of the smallest paper Björn has
    a_width = 2 ** (-5/4)
    a_height = 2 ** (-3/4)
    a_area = a_width * a_height

    # Check if Björn has enough paper to make an A1 paper
    total_area = 0
    for i in range(n - 1):
        total_area += a_area * sheets[i] * 2 ** ((i + 2) / 4)

    if total_area >= a1_area:
        # Calculate the total length of tape needed
        total_length = 0
        for i in range(n - 1):
            total_length += a_width * sheets[i] * 2 ** ((i + 1) / 4)

        print(total_length)
    else:
        print("impossible")

if __name__ == "__main__":
    main()