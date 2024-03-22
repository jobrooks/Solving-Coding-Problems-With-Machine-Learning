# 4.2 Time Limit Exception 6/22
n = int(input())  # read the number of food trucks

# create two lists to store the street and avenue coordinates of the food trucks
streets = []
avenues = []

# read the coordinates of the food trucks and store them in the lists
for i in range(n):
    s, a = map(int, input().split())
    streets.append(s)
    avenues.append(a)

# initialize the total distance to zero
total_distance = 0

# iterate over all pairs of food trucks
for i in range(n):
    for j in range(i + 1, n):  # only consider distinct pairs
        # calculate the distance between the two food trucks and add it to the total distance
        distance = abs(streets[i] - streets[j]) + abs(avenues[i] - avenues[j])
        total_distance += distance

# print the total distance
print(total_distance)
