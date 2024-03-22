# Difficulty: 2.6
# Result: Wrong answer
# Tests passed: 0/13
# Error: none
# Response: 
def find_all_knowing_villagers(num_villagers, num_evenings, evenings):
  """
  Finds villagers who know all songs sung during evenings.

  Args:
      num_villagers: Total number of villagers (integer).
      num_evenings: Number of evenings (integer).
      evenings: List of lists representing villagers present each evening.

  Returns:
      A list of villager numbers (integers) who know all songs.
  """

  # Initialize set to store songs sung on each evening
  songs_sung_each_evening = [set() for _ in range(num_evenings)]

  # Identify songs sung on evenings with the bard
  for i, evening in enumerate(evenings):
    if 1 in evening:  # Check if bard is present (villager number 1)
      songs_sung_each_evening[i] = set(evening)  # New unique song by bard
    else:
      # Villagers exchange songs, all songs sung that evening
      songs_sung_each_evening[i] = set.union(*[songs_sung_each_evening[j] for j in range(i)])

  # Find villagers who were present at all evenings with songs
  all_knowing_villagers = set(range(1, num_villagers + 1))  # Include bard (villager 1)
  for songs_sung in songs_sung_each_evening:
    all_knowing_villagers &= songs_sung  # Intersection: villagers present at all evenings with songs

  return sorted(list(all_knowing_villagers))  # Sort and return villager numbers

# Get number of villagers and evenings
num_villagers = int(input())
num_evenings = int(input())

# Read list of villagers present each evening
evenings = []
for _ in range(num_evenings):
  num_present, *present_villagers = map(int, input().split())
  evenings.append(present_villagers)

# Find and print villagers who know all songs
all_knowing_villagers = find_all_knowing_villagers(num_villagers, num_evenings, evenings)
for villager in all_knowing_villagers:
  print(villager)
