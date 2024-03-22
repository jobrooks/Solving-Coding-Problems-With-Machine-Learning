# 2.1 run-time error 0/2

import sys
import math

EPSILON = 1e-9

# Helper function to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Main function to process each test case
def process_test_case():
    # Read input for a single test case
    d, n = map(int, input().split())
    if d == 0 and n == 0:
        # End of input
        return False
    hives = [tuple(map(float, input().split())) for _ in range(n)]

    # Initialize counters for sweet and sour honey
    sweet = 0
    sour = 0

    # Check each pair of hives
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the distance between the hives
            dist = distance(hives[i][0], hives[i][1], hives[j][0], hives[j][1])
            if dist <= d + EPSILON:
                # Hives are too close together and will fight
                sour += 2

    # Calculate the number of hives that will produce sweet honey
    sweet = n - sour

    # Output the results for this test case
    print(f"{sour} sour, {sweet} sweet")

    return True

# Main loop to process all test cases
while process_test_case():
    pass
