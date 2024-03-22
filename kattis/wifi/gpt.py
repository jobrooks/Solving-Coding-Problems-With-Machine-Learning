# 4.5 wrong answer 0/3
import math

def can_cover(houses, n, m, x):
    cnt = 1
    pos = houses[0]
    for i in range(1, m):
        if houses[i] - pos > x:
            cnt += 1
            pos = houses[i]
            if cnt > n:
                return False
    return True

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    houses = [int(input()) for _ in range(m)]
    houses.sort()
    l, r = 0, houses[-1]
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if can_cover(houses, n, m, mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print("{:.1f}".format(math.ceil(ans*10)/10))  # Round up to nearest tenth
