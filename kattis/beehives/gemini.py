# Difficulty: 5.3
# Result: Run-time error 
# Tests passed: 0/53
# Error: run-time
# Response: 
def count_honey_production(fighting_distance, num_hives, hive_locations):
  """
  Counts the number of hives producing sour and sweet honey.

  Args:
      fighting_distance: Float representing the distance within which hives fight.
      num_hives: Integer representing the number of hives.
      hive_locations: List of tuples (x, y) representing hive positions.

  Returns:
      A tuple (sour_honey, sweet_honey) representing the number of hives with sour 
      and sweet honey, respectively.
  """

  sour_honey = 0
  sweet_honey = 0

  # Check each hive against all other hives
  for i in range(num_hives):
    hive_x, hive_y = hive_locations[i]
    fighting = False
    for j in range(i + 1, num_hives):
      other_x, other_y = hive_locations[j]
      # Calculate distance between current hive and another hive
      distance = ((hive_x - other_x) ** 2 + (hive_y - other_y) ** 2) ** 0.5
      if distance <= fighting_distance:
        fighting = True
        break  # Stop checking other hives if fighting is found

    if fighting:
      sour_honey += 2  # Both hives fight and produce sour honey
    else:
      sweet_honey += 1  # Hive doesn't fight and produces sweet honey

  return sour_honey, sweet_honey

# Loop until end of input is reached
while True:
  # Read fighting distance and number of hives
  try:
    fighting_distance, num_hives = map(float, input().split())
  except ValueError:
    break  # Exit loop on invalid input (likely end of input)
  if fighting_distance <= 0 or num_hives <= 0:
    break  # Exit loop on invalid values (shouldn't happen)

  # Read hive locations
  hive_locations = []
  for _ in range(int(num_hives)):
    hive_x, hive_y = map(float, input().split())
    hive_locations.append((hive_x, hive_y))

  # Count sour and sweet honey
  sour_honey, sweet_honey = count_honey_production(fighting_distance, num_hives, hive_locations)

  # Print results
  print(f"{sour_honey} sour, {sweet_honey} sweet")
