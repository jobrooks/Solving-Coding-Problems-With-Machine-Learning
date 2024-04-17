import math

def distance(lat1, lon1, lat2, lon2):
  """Calculates the distance between two points on a sphere."""
  # Convert latitudes and longitudes to radians
  lat1 = math.radians(lat1)
  lon1 = math.radians(lon1)
  lat2 = math.radians(lat2)
  lon2 = math.radians(lon2)

  # Calculate the distance using the Haversine formula
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
  return 6371 * c  # Distance in kilometers

def find_hub(airports):
  """Finds the airport that minimizes the maximum direct flying distance to all other airports."""
  # Calculate the distance matrix between all pairs of airports
  distances = [[distance(lat1, lon1, lat2, lon2) for lat2, lon2 in airports] for lat1, lon1 in airports]

  # Find the airport with the minimum maximum distance
  min_max_distance = float('inf')
  hub = None
  for i in range(len(airports)):
    max_distance = max(distances[i])
    if max_distance < min_max_distance:
      min_max_distance = max_distance
      hub = airports[i]

  return hub

def main():
  # Read the input
  with open('input.txt', 'r') as f:
    lines = f.readlines()

  # Parse the input and find the hub for each set of airports
  for line in lines:
    n = int(line.strip())
    airports = []
    for i in range(n):
      lat, lon = map(float, f.readline().strip().split())
      airports.append((lat, lon))

    hub = find_hub(airports)

    # Print the latitude and longitude of the hub
    print('{:.2f} {:.2f}'.format(hub[0], hub[1]))

if __name__ == '__main__':
  main()