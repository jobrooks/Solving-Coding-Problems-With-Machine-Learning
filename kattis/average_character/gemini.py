# Difficulty: 1.9
# Justification: 
# Result: passed
# Tests passed: 32/32
# Error: none
# Response: 
def average_ascii(text):
  """
  Calculates the average ASCII character of a string, truncating downwards.

  Args:
      text: The input string (string).

  Returns:
      The average ASCII character (single character).
  """

  # Calculate total ASCII value and string length
  total_ascii = sum(ord(char) for char in text if char.isprintable())
  length = len(text)

  # Handle empty string or strings without printable characters
  if length == 0 or total_ascii == 0:
    return chr(32)  # Return space character for empty or non-printable strings

  # Calculate average ASCII value (truncate towards smaller integer)
  average_ascii_value = total_ascii // length

  # Return the average character as a single character
  return chr(average_ascii_value)

# Read input text
text = input()

# Calculate and print the average ASCII character
average_char = average_ascii(text)
print(average_char)
