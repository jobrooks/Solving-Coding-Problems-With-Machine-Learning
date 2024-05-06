# 8.5 Error 1/2
import sys

def main():
    for line in sys.stdin:
        if line == "0 0 0\n":
            break

        # Read the three dice.
        d1 = [int(x) for x in line.split()]
        d2 = [int(x) for x in sys.stdin.readline().split()]
        d3 = [int(x) for x in sys.stdin.readline().split()]

        # Read the die to simulate.
        target = [int(x) for x in sys.stdin.readline().split()]

        # Check if it is possible to simulate the die.
        if check(d1, d2, d3, target):
            print("YES")
        else:
            print("NO")

def check(d1, d2, d3, target):
    # Normalize the probabilities.
    for die in [d1, d2, d3]:
        total = sum(die)
        for i in range(3):
            die[i] /= total

    # Check if the probabilities are feasible.
    for i in range(3):
        if target[i] < d1[i] or target[i] > d1[i] + d2[i] + d3[i]:
            return False

    # Find the probabilities of rolling each die.
    p1 = (target[0] - d1[0]) / (d2[0] + d3[0])
    p2 = (target[1] - d1[1] - d2[1]) / d3[1]
    p3 = (target[2] - d1[2] - d2[2] - d3[2]) / 0

    # Check if the probabilities are valid.
    if p1 < 0 or p1 > 1 or p2 < 0 or p2 > 1 or p3 < 0 or p3 > 1:
        return False

    return True

if __name__ == "__main__":
    main()