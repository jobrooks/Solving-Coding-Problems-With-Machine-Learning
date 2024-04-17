import sys

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def area(polygon):
    n = len(polygon)
    area = 0.0
    for i in range(n):
        area += cross(polygon[i], polygon[(i + 1) % n], polygon[(i + 2) % n])
    return abs(area) / 2.0

def main():
    n = int(input())
    polygons = []
    for _ in range(n):
        m = int(input())
        polygon = []
        for _ in range(m):
            x, y = map(int, input().split())
            polygon.append((x, y))
        polygons.append(polygon)

    paint = 0.0
    canvas = 0.0
    for polygon in polygons:
        paint += area(polygon)
        canvas += area(polygon) / 2.0

    print('{:.6f} {:.6f}'.format(paint, canvas))

if __name__ == "__main__":
    main()