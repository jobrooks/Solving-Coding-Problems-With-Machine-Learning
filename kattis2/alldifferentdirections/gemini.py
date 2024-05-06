import math

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate over each test case
    for i in range(num_test_cases):
        # Read the number of people to ask for directions
        num_people = int(input())

        # Initialize the average destination and maximum distance
        avg_x = 0
        avg_y = 0
        max_distance = 0

        # Iterate over each person's directions
        for j in range(num_people):
            # Read the person's location and directions
            x, y = map(float, input().split())
            directions = input().split()

            # Initialize the current destination
            current_x = x
            current_y = y
            current_dir = 0

            # Iterate over each instruction in the directions
            for direction in directions:
                # Check if the instruction is a start instruction
                if direction.startswith("start"):
                    # Set the current direction to the specified angle
                    current_dir = float(direction[6:])
                # Check if the instruction is a turn instruction
                elif direction.startswith("turn"):
                    # Rotate the current direction by the specified angle
                    current_dir += float(direction[5:])
                # Check if the instruction is a walk instruction
                elif direction.startswith("walk"):
                    # Move the current destination in the current direction by the specified distance
                    current_x += float(direction[5:]) * math.cos(math.radians(current_dir))
                    current_y += float(direction[5:]) * math.sin(math.radians(current_dir))

            # Update the average destination
            avg_x += current_x / num_people
            avg_y += current_y / num_people

            # Update the maximum distance
            max_distance = max(max_distance, math.sqrt((current_x - avg_x)**2 + (current_y - avg_y)**2))

        # Print the average destination and maximum distance
        print(f"{avg_x:.2f} {avg_y:.2f} {max_distance:.2f}")

if __name__ == "__main__":
    main()