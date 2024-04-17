import math
test_cases = int(input())
for test_case in range(test_cases):
    n = int(input())
    if n == 0:
        break
    x, y = map(float, input().split())
    directions = []
    for _ in range(n):
        directions.append(input().split())
    avg_x, avg_y = 0, 0
    for direction in directions:
        angle = float(direction[1]) * math.pi / 180
        if direction[0] == 'start':
            avg_x += x * math.cos(angle) + y * math.sin(angle)
            avg_y += -x * math.sin(angle) + y * math.cos(angle)
        elif direction[0] == 'turn':
            angle = float(direction[1]) * math.pi / 180
            for i in range(1, len(directions)):
                x_, y_ = directions[i][1], directions[i][2]
                directions[i][1] = x_ * math.cos(angle) - y_ * math.sin(angle)
                directions[i][2] = x_ * math.sin(angle) + y_ * math.cos(angle)
        elif direction[0] == 'walk':
            distance = float(direction[1])
            avg_x += distance * math.cos(angle)
            avg_y += distance * math.sin(angle)
    avg_x /= n
    avg_y /= n
    max_distance = 0
    for direction in directions:
        x_, y_ = float(direction[1]), float(direction[2])
        distance = math.sqrt((x_ - avg_x)**2 + (y_ - avg_y)**2)
        max_distance = max(max_distance, distance)
    print(f"{avg_x:.4f} {avg_y:.4f} {max_distance:.4f}")