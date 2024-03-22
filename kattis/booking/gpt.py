# 5.6 runtime error 0/9
import datetime
import math

def parse_datetime(dt_str):
    return datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M')

def calculate_rooms_needed(bookings, cleaning_time):
    # create a list to keep track of the number of bookings for each minute
    start_time = datetime.datetime(2013, 1, 1)
    end_time = datetime.datetime(2017, 1, 1)
    num_minutes = int((end_time - start_time).total_seconds() / 60)
    num_bookings = [0] * num_minutes

    # iterate over the bookings and increment the number of bookings for each minute
    for booking in bookings:
        start = parse_datetime(booking[1])
        end = parse_datetime(booking[2])
        start_index = int((start - start_time).total_seconds() / 60)
        end_index = int((end - start_time).total_seconds() / 60)
        for i in range(start_index, end_index):
            num_bookings[i] += 1

    # calculate the maximum number of bookings for any minute
    max_bookings = max(num_bookings)

    # calculate the number of rooms needed
    rooms_needed = math.ceil(max_bookings / (24 * 60 / cleaning_time))

    return rooms_needed

# read the number of test cases
num_cases = int(input())

# iterate over the test cases
for i in range(num_cases):
    # read the input for this test case
    num_bookings, cleaning_time = map(int, input().split())
    bookings = [input().split() for j in range(num_bookings)]

    # calculate the minimum number of rooms needed
    rooms_needed = calculate_rooms_needed(bookings, cleaning_time)

    # print the result
    print(rooms_needed)
