# Difficulty:2.3
# Result: wrong answer 
# Tests passed: 0/24
# Error: none
# Response: 
def baby_panda_sneezes(n, m):
  """
  Calculates the number of times the baby panda sneezed based on slimes after n days.

  Args:
      n: Number of days (integer).
      m: Number of slimes after n days (even integer).

  Returns:
      The number of times the baby panda sneezed (integer).
  """

  # Check for invalid input (m must be even)
  if m % 2 != 0:
    return "Invalid Input: Number of slimes (m) must be even."

  # Calculate number of sneezes (number of doublings)
  sneezes = 0
  current_slimes = m
  while current_slimes > 0:
    current_slimes //= 2  # Integer division for number of doublings
    sneezes += 1

  return sneezes

# Get user input
try:
  n = int(input("Enter the number of days (n): "))
  m = int(input("Enter the number of slimes after n days (m - must be even): "))
except ValueError:
  print("Invalid input: Please enter integers for n and m.")
  exit()

# Check for valid input (m must be even)
if m % 2 != 0:
  print("Invalid Input: Number of slimes (m) must be even.")
  exit()

# Calculate and print number of sneezes
number_of_sneezes = baby_panda_sneezes(n, m)
print("The baby panda sneezed", number_of_sneezes, "times.")
