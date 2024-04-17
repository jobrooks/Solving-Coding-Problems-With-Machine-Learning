import math

def main():
    # Get the input
    M, N, R = map(int, input().split())
    a_x, a_y, b_x, b_y = map(int, input().split())

    # Calculate the distance between the two points
    distance = math.sqrt((R * math.sin(math.pi * (b_x - a_x) / M))**2 + (R * math.cos(math.pi * (b_y - a_y) / N))**2)

    # Print the distance
    print(distance)

if __name__ == "__main__":
    main()