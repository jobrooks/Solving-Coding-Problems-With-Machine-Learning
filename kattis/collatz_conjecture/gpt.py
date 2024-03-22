# 4.2 Wrong Answer 0/2

# define a function to compute the Collatz sequence of a given starting value
def collatz_sequence(x):
    sequence = [x]  # initialize the sequence with the starting value
    while x != 1:  # keep iterating until the sequence reaches 1
        if x % 2 == 0:  # if the current value is even, divide by 2
            x //= 2
        else:  # if the current value is odd, multiply by 3 and add 1
            x = 3 * x + 1
        sequence.append(x)  # add the new value to the sequence
    return sequence

# read the first pair of starting values
a, b = map(int, input().split())

# loop until both starting values are zero
while a != 0 or b != 0:
    # compute the Collatz sequences of both starting values
    seq_a = collatz_sequence(a)
    seq_b = collatz_sequence(b)

    # find the first number that occurs in both sequences
    intersection = set(seq_a).intersection(seq_b)
    c = min(intersection)  # choose the smallest number as the intersection

    # compute the number of steps needed in both sequences to reach the intersection
    sa = seq_a.index(c)
    sb = seq_b.index(c)

    # print the result in the required format
    print(f"{a} needs {sa} steps, {b} needs {sb} steps, they meet at {c}")

    # read the next pair of starting values
    a, b = map(int, input().split())
