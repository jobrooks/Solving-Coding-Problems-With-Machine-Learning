# Difficulty: 2.2
# Justification: 
# Result: Wrong Answer
# Tests passed: 0/47
# Error: none
# Response: 
def max_saved_unlocks(researchers, auto_lock_time):
  """
  Calculates the maximum number of unlockings Penelope can save.

  Args:
      researchers: A list of tuples (arrival_time, stay_time) for each researcher.
      auto_lock_time: The number of minutes after which a workstation locks (integer).

  Returns:
      The maximum number of unlockings Penelope can save (integer).
  """

  # Sort researchers by their departure time (finish time)
  researchers.sort(key=lambda x: x[0] + x[1])

  # Initialize variables
  unlocked_workstations = 0
  saved_unlocks = 0
  current_time = 0

  # Iterate through researchers
  for arrival_time, stay_time in researchers:
    # Update current time (account for idle periods)
    current_time = max(current_time, arrival_time)

    # Unlock workstation if previous one timed out
    if current_time - arrival_time > auto_lock_time:
      unlocked_workstations += 1

    # Assign researcher to an unlocked workstation
    saved_unlocks += 1

    # Update current time based on researcher's stay
    current_time += stay_time

  return saved_unlocks

# Read input
num_researchers, auto_lock_time = map(int, input().split())
researchers = []
for _ in range(num_researchers):
  arrival_time, stay_time = map(int, input().split())
  researchers.append((arrival_time, stay_time))

# Calculate and print the maximum saved unlockings
max_unlocks_saved = max_saved_unlocks(researchers, auto_lock_time)
print(max_unlocks_saved)
