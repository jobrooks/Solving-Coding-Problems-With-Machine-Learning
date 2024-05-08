import sys

input = sys.stdin.readline

N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for i in range(N)]

# Compute the cross product of two points
def cross(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

# Check if a point is inside a triangle
def inside_triangle(p, a, b, c):
    return (cross(b - a, p - a) > 0 and
            cross(c - b, p - b) > 0 and
            cross(a - c, p - c) > 0)

# Find the minimum number of posters to cover all interior points
def min_posters(points, K):
    # Sort the points by their y-coordinates
    points.sort(key=lambda p: p[1])

    # Initialize the set of covered points
    covered = set()

    # Iterate over the points from bottom to top
    for i in range(N):
        # If the point is not covered, add it to the set of covered points
        if points[i] not in covered:
            covered.add(points[i])

            # If the number of covered points is greater than or equal to K, return
            if len(covered) >= K:
                return covered

    # Return the set of covered points
    return covered


# Find the vertices to place posters on
def find_vertices(points, covered):
    # Initialize the set of vertices
    vertices = set()

    # Iterate over the covered points
    for point in covered:
        # Find the three vertices that form the triangle that contains the point
        for i in range(N):
            a, b, c = points[i], points[(i + 1) % N], points[(i + 2) % N]
            if inside_triangle(point, a, b, c):
                # Add the three vertices to the set of vertices
                vertices.add(i + 1)
                vertices.add((i + 1) % N + 1)
                vertices.add((i + 2) % N + 1)
                break

    # Return the set of vertices
    return vertices


# Compute the minimum number of posters to cover all interior points
covered = min_posters(points, K)

# Find the vertices to place posters on
vertices = find_vertices(points, covered)

# Output the vertices
print(*vertices)