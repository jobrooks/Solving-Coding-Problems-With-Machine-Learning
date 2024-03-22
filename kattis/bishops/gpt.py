# 2.3 accepted 3/3

import sys

def max_bishops(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2*n - 2

for line in sys.stdin:
    n = int(line.strip())
    print(max_bishops(n))