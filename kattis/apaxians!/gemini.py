# Difficulty: 1.4
# Justification: 
# Result: passed
# Tests passed: 41/41
# Error: none
# Response: 
def compact_apaxian_name(name):
  """
  Converts an Apaxian name to its compact form (removing consecutive duplicate letters).

  Args:
      name: A string representing the Apaxian name (lowercase letters only).

  Returns:
      A string representing the compact form of the name.
  """

  # Initialize variables
  compacted_name = ""
  prev_char = None

  # Iterate through each character in the name
  for char in name:
    # Check if the character is different from the previous one
    if char != prev_char:
      compacted_name += char  # Add the character to the compacted name
    prev_char = char  # Update the previous character

  return compacted_name

# Read input name
name = input()

# Get the compact form of the name
compacted_name = compact_apaxian_name(name)

# Print the compacted name
print(compacted_name)
