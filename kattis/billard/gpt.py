# 1.8 wrong answer 0/2

import math

while True:
    a, b, s, m, n = map(int, input().split())
    if a == b == s == m == n == 0:
        break
    
    x = a * m
    y = b * n
    t = s / math.sqrt(x**2 + y**2)
    vx = x * t
    vy = y * t
    v0 = math.sqrt(vx**2 + vy**2)
    angle = math.degrees(math.atan2(vy, vx))
    
    print("{:.2f} {:.2f}".format(angle, v0))
