import math

def main():
    n = int(input())
    papers = [int(x) for x in input().split()]

    # Check if there are enough papers to make an A1 paper
    if sum(papers) == 0:
        print("impossible")
        return

    # Calculate the length of the A1 paper
    a1_length = 2**(-5/4) * 2**(-3/4)

    # Calculate the length of the tape needed to join the papers together
    tape_length = 0
    for i in range(n-1, 0, -1):
        if papers[i] > 0:
            tape_length += a1_length * (2**(i-1)/2) * papers[i]
            a1_length *= 2**(1/4)

    # Print the length of the tape
    print("{:.10f}".format(tape_length))

if __name__ == "__main__":
    main()