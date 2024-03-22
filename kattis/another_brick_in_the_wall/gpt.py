# 2.1 accepted 30/30

h, w, n = map(int, input().split())
bricks = list(map(int, input().split()))

current_row = 0
current_width = 0

while current_row < h:
    current_layer = []
    while current_width < w:
        if not bricks:
            print("NO")
            exit()
        brick = bricks.pop(0)
        if current_width + brick > w:
            break
        current_layer.append(brick)
        current_width += brick
    if current_width != w:
        break
    current_row += 1
    current_width = 0

if current_row == h:
    print("YES")
else:
    print("NO")
