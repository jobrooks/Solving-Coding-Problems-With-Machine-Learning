# 1.3 wrong answer 1/20

import math

n = int(input())
revolutions = n / 4  # Each revolution produces four ticks
print('{:.2f}'.format(math.ceil(revolutions) if revolutions % 1 >= 0.5 else math.floor(revolutions)))
