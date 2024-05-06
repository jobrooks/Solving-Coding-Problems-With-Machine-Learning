import math

def main():
    # Read the number of vertices in the polygon
    n = int(input())

    # Read the coordinates of the polygon vertices
    vertices = []
    for i in range(n):
        vertices.append(tuple(map(int, input().split())))

    # Initialize the maximum length of the landing strip
    max_length = 0

    # Iterate over all pairs of vertices
    for i in range(n):
        for j in range(i + 1, n):
            # Compute the length of the landing strip between vertices i and j
            length = math.sqrt((vertices[i][0] - vertices[j][0])**2 + (vertices[i][1] - vertices[j][1])**2)

            # Check if the landing strip intersects the polygon
            intersects = False
            for k in range(n):
                if k == i or k == j:
                    continue
                if is_intersecting(vertices[i], vertices[j], vertices[k]):
                    intersects = True
                    break

            # Update the maximum length of the landing strip if it does not intersect
            if not intersects:
                max_length = max(max_length, length)

    # Print the maximum length of the landing strip
    print(max_length)

# Check if two line segments intersect
def is_intersecting(p1, p2, p3):
    # Check if the two line segments are colinear
    if (p1[0] - p2[0]) * (p3[1] - p2[1]) == (p3[0] - p2[0]) * (p1[1] - p2[1]):
        return False

    # Check if the two line segments intersect at the endpoints
    if (p1[0] <= p3[0] <= p2[0] or p1[0] >= p3[0] >= p2[0]) and (p1[1] <= p3[1] <= p2[1] or p1[1] >= p3[1] >= p2[1]):
        return True

    # Compute the cross product of the vectors formed by the line segments
    cross_product = (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    # Check if the cross product is zero, which indicates that the line segments are parallel
    if cross_product == 0:
        return False

    # Check if the cross product is positive, which indicates that the line segments intersect on the left side
    if cross_product > 0:
        return True

    # Otherwise, the line segments intersect on the right side
    return False

if __name__ == "__main__":
    main()