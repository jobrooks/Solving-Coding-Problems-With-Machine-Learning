# 4.0 wrong answer 0/13

import math

# read input
n = int(input())
counts = list(map(int, input().split()))

# define A1 dimensions
A1_width = 2**(-3/4)
A1_height = 2**(-1/4)

# initialize current paper dimensions and total tape length
width = 2**(-5/4)
height = 2**(-3/4)
tape_length = 0

# iterate over paper sizes in reverse order
for count in reversed(counts):
    # if we need more paper than we have, it's impossible to make A1
    if count <= 0:
        print("impossible")
        exit()

    # calculate how many papers of the current size we need
    num_needed = math.ceil(count / 2)

    # calculate the dimensions of the required paper
    new_width, new_height = height, width * 2

    # add up the tape length required to join the papers
    tape_length += num_needed * width

    # update the current paper dimensions
    width, height = new_width, new_height

# if we have enough paper, calculate the total tape length required for A1
if width >= A1_width and height >= A1_height:
    tape_length += (width - A1_width) * height
    print("{:.6f}".format(tape_length))
else:
    print("impossible")
