import math

def distance(M, N, R, a_x, a_y, b_x, b_y):
    """Computes the distance between two street corners in Amsterdam.

    Args:
        M: The number of segments (or ‘pie slices’) the model of the city is split into.
        N: The number of half rings the model of the city is split into.
        R: The radius of the city, given with at most 15 digits after the decimal point.
        a_x: The x-coordinate of the first corner.
        a_y: The y-coordinate of the first corner.
        b_x: The x-coordinate of the second corner.
        b_y: The y-coordinate of the second corner.

    Returns:
        The least distance needed to travel from point a to point b following only the streets in the model.
    """

    # Convert the coordinates to polar coordinates.
    a_r = math.sqrt(a_x**2 + a_y**2)
    a_theta = math.atan2(a_y, a_x)
    b_r = math.sqrt(b_x**2 + b_y**2)
    b_theta = math.atan2(b_y, b_x)

    # Compute the distance between the two points in polar coordinates.
    d_r = abs(a_r - b_r)
    d_theta = abs(a_theta - b_theta)

    # Convert the distance back to Cartesian coordinates.
    d_x = d_r * math.cos(d_theta)
    d_y = d_r * math.sin(d_theta)

    # Return the distance.
    return math.sqrt(d_x**2 + d_y**2)


def main():
    """Gets the input and calls the distance function."""

    # Get the input.
    M, N, R = map(int, input().split())
    a_x, a_y, b_x, b_y = map(int, input().split())

    # Compute the distance.
    d = distance(M, N, R, a_x, a_y, b_x, b_y)

    # Print the distance.
    print(d)


if __name__ == "__main__":
    main()