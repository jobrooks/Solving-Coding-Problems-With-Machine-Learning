# 6.9 Error 1/22
import math

def main():
    # Read the input
    n = int(input())
    polygons = []
    for _ in range(n):
        m = int(input())
        vertices = []
        for _ in range(m):
            x, y = map(int, input().split())
            vertices.append((x, y))
        polygons.append(vertices)

    # Calculate the total amount of paint used and the total amount of canvas covered
    total_paint = 0
    total_canvas = 0
    for polygon in polygons:
        # Calculate the area of the polygon
        area = 0
        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]
            area += (x1 * y2 - x2 * y1)
        area = abs(area) / 2

        # Calculate the perimeter of the polygon
        perimeter = 0
        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]
            perimeter += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # Update the total paint and canvas
        total_paint += area
        total_canvas += perimeter

    # Print the output
    print(total_paint)
    print(total_canvas)

if __name__ == "__main__":
    main()