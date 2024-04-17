def main():
    # Get the number of minions
    num_minions = int(input())

    # Get the temperature preferences of each minion
    preferences = []
    for i in range(num_minions):
        preferences.append(list(map(int, input().split())))

    # Sort the preferences by the lower bound
    preferences.sort(key=lambda x: x[0])

    # Initialize the number of rooms
    num_rooms = 0

    # Initialize the current room's temperature range
    current_room = [preferences[0][0], preferences[0][1]]

    # Iterate over the remaining preferences
    for i in range(1, num_minions):
        # If the current room's temperature range overlaps with the next minion's preference, extend the range
        if current_room[1] >= preferences[i][0]:
            current_room[1] = max(current_room[1], preferences[i][1])
        # Otherwise, create a new room
        else:
            num_rooms += 1
            current_room = [preferences[i][0], preferences[i][1]]

    # Output the number of rooms
    print(num_rooms)


if __name__ == "__main__":
    main()