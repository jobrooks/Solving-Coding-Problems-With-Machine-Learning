# 3.5 wrong answer 0/4

import sys

# function to convert hh:mm:ss format to seconds
def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

# initialize variables
prev_time = 0
prev_speed = 0
prev_distance = 0

# process input
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if ' ' in line:
        # speed change
        time_str, speed_str = line.split()
        time = time_to_seconds(time_str)
        distance = prev_distance + (time - prev_time) * prev_speed / 3600
        prev_time = time
        prev_speed = int(speed_str)
        prev_distance = distance
    else:
        # distance query
        time_str = line
        time = time_to_seconds(time_str)
        distance = prev_distance + (time - prev_time) * prev_speed / 3600
        print(time_str, '%.2f' % distance)
