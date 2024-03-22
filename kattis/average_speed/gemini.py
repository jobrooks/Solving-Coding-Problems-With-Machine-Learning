# Difficulty: 3.7
# Justification: 
# Result: Run-time Error
# Tests passed: 0/4
# Error: Run-time Error
# Response: 
def average_speed(data):
  """
  Calculates the average speed for a car trip based on speed changes and elapsed times.

  Args:
      data: A list of tuples containing (elapsed_time, speed) data points.

  Returns:
      A list of tuples containing (elapsed_time, distance) data points.
  """

  # Initialize variables
  distance = 0
  prev_time = None
  results = []

  # Iterate through speed change data points
  for elapsed_time, speed in data:
    # Convert elapsed time string to seconds
    time_in_seconds = sum(int(x) * 60**i for i, x in enumerate(elapsed_time.split(":")[::-1]))

    # Calculate distance traveled since last speed change
    if prev_time is not None:
      time_delta = time_in_seconds - prev_time
      distance += speed * time_delta / 3600  # Convert speed from km/h to m/s and multiply by time

    # Update previous time and append result (elapsed time, distance)
    prev_time = time_in_seconds
    results.append((elapsed_time, round(distance, 2)))

  return results

# Read speed change data points
data = []
while True:
  line = input().strip()
  if not line:
    break  # Empty line indicates end of data
  elapsed_time, speed = line.split()
  data.append((elapsed_time, int(speed)))  # Convert speed to integer

# Calculate and print average speed data points
average_speed_data = average_speed(data)
for elapsed_time, distance in average_speed_data:
  print(elapsed_time, distance)
