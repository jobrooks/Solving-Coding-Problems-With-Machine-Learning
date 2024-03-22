# 1.5 accepted 63/63 

r, f = map(int, input().split())

total_rotation_angle = (f // r) * 180
if (f % r) >= r/2:
    total_rotation_angle += 180

if total_rotation_angle % 360 == 0:
    print("up")
else:
    print("down")
