# 1.7 accepted 23/23

r, n = map(int, input().split())
booked = set(int(input()) for _ in range(n))

for i in range(1, r + 1):
    if i not in booked:
        print(i)
        break
else:
    print("too late")
