# 4.2 wrong answer 0/3
import sys

def lowest_non_zero_digit(n):
    if n == 0:
        return 1
    else:
        # Find the lowest non-zero digit of n!
        last_digit = 1
        for i in range(2, n+1):
            # Multiply last_digit by i and reduce it to a single digit
            last_digit = (last_digit * i) % 10
            if last_digit == 0:
                # If the last digit becomes zero, divide by 10 to remove the zero
                last_digit = 1
                while i % 10 == 0:
                    i //= 10
                last_digit *= i % 10
        return last_digit

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    print(lowest_non_zero_digit(n))
