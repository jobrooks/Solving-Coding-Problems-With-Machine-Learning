# 1.7 accepted 2/2

while True:
    w, l = map(int, input().split())
    if w == 0 and l == 0:
        break

    n = int(input())
    x_robot, y_robot = 0, 0
    x_actual, y_actual = 0, 0

    for _ in range(n):
        direction, distance = input().split()
        distance = int(distance)

        if direction == "u":
            y_actual += distance
            y_robot = min(y_robot + distance, l-1)
        elif direction == "d":
            y_actual -= distance
            y_robot = max(y_robot - distance, 0)
        elif direction == "r":
            x_actual += distance
            x_robot = min(x_robot + distance, w-1)
        else:
            x_actual -= distance
            x_robot = max(x_robot - distance, 0)

    print("Robot thinks", x_actual, y_actual)
    print("Actually at", x_robot, y_robot)
    print()
