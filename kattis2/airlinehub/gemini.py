import math

def distance(lat1, lon1, lat2, lon2):
  """
  Calculates the distance between two points on the Earth's surface using the
  Haversine formula.

  Args:
    lat1: The latitude of the first point in degrees.
    lon1: The longitude of the first point in degrees.
    lat2: The latitude of the second point in degrees.
    lon2: The longitude of the second point in degrees.

  Returns:
    The distance between the two points in kilometers.
  """

  # Convert the latitudes and longitudes to radians.
  lat1 = math.radians(lat1)
  lon1 = math.radians(lon1)
  lat2 = math.radians(lat2)
  lon2 = math.radians(lon2)

  # Calculate the difference between the latitudes and longitudes.
  dlat = lat2 - lat1
  dlon = lon2 - lon1

  # Calculate the Haversine formula.
  a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(
      dlon / 2) ** 2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  # Calculate the distance in kilometers.
  distance = 6371 * c

  return distance

def main():
  """
  Finds the airport that best serves as a hub for World Wide Flyer.

  Args:
    None.

  Returns:
    None.
  """

  # Read the input data.
  n = int(input())
  airports = []
  for i in range(n):
    lat, lon = map(float, input().split())
    airports.append((lat, lon))

  # Find the airport that minimizes the maximum direct flying distance from the
  # hub to any other airport in the world.
  min_max_distance = float('inf')
  hub_airport = None
  for airport in airports:
    max_distance = 0
    for other_airport in airports:
      if airport == other_airport:
        continue
      max_distance = max(max_distance, distance(airport[0], airport[1],
                                               other_airport[0],
                                               other_airport[1]))
    if max_distance < min_max_distance:
      min_max_distance = max_distance
      hub_airport = airport

  # Print the latitude and longitude of the airport that best serves as a hub.
  print("{0:.2f} {1:.2f}".format(hub_airport[0], hub_airport[1]))

if __name__ == "__main__":
  main()