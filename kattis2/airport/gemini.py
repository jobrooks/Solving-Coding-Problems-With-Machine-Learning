import sys
from typing import List, Tuple

def cross(o: Tuple[float, float], a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Returns the cross product of the vector oa and the vector ob.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dot(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Returns the dot product of the vectors a and b.
    """
    return a[0] * b[0] + a[1] * b[1]

def dist2(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Returns the squared distance between the points a and b.
    """
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx*dx + dy*dy

def project_point_on_line(p: Tuple[float, float], a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    """
    Projects the point p onto the line defined by the points a and b.
    """
    ab = b[0] - a[0], b[1] - a[1]
    ap = p[0] - a[0], p[1] - a[1]
    dot_ab_ap = dot(ab, ap)
    ab_norm_sqr = dot(ab, ab)
    return [a[0] + dot_ab_ap / ab_norm_sqr * ab[0], a[1] + dot_ab_ap / ab_norm_sqr * ab[1]]

def get_squared_length_of_longest_landing_strip(polygon: List[Tuple[float, float]]) -> float:
    """
    Returns the squared length of the longest landing strip that can be built on the island.
    """
    n = len(polygon)

    # Find the convex hull of the polygon.
    hull = []
    for i in range(n):
        while len(hull) >= 2 and cross(hull[-2], hull[-1], polygon[i]) <= 0:
            hull.pop()
        hull.append(polygon[i])

    # Find the longest line segment in the convex hull.
    max_dist2 = 0
    for i in range(len(hull)):
        for j in range(i+1, len(hull)):
            max_dist2 = max(max_dist2, dist2(hull[i], hull[j]))

    # Check if any of the edges of the polygon are intersected by a line longer than the longest line segment in the convex hull.
    for i in range(n):
        for j in range(i+1, n):
            a, b = polygon[i], polygon[j]
            for k in range(len(hull)):
                l, r = hull[k], hull[(k+1) % len(hull)]
                if cross(a, b, l) * cross(a, b, r) <= 0 and cross(l, r, a) * cross(l, r, b) <= 0:
                    max_dist2 = max(max_dist2, dist2(project_point_on_line(l, a, b), project_point_on_line(r, a, b)))

    return max_dist2

def main():
    n = int(sys.stdin.readline())
    polygon = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    max_dist2 = get_squared_length_of_longest_landing_strip(polygon)
    print(max_dist2**0.5)

if __name__ == "__main__":
    main()