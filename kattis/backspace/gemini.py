# Difficulty: 2.1
# Result: Accepted
# Tests passed: 25/25
# Error: none
# Response: 
def fix_backspace(text):
  """
  Corrects the broken backspace key by removing '<' characters.

  Args:
      text: The string written in the editor with '<' replacing backspaces (string).

  Returns:
      The string as Bjarki intended to write it (string).
  """

  # Use a list for efficient insertion and deletion operations
  corrected_text = []
  for char in text:
    if char != "<":
      corrected_text.append(char)
    else:
      # Remove the last character (intended backspace) if it exists
      if corrected_text:
        corrected_text.pop()

  # Return the corrected string joined from the list
  return "".join(corrected_text)

# Read the text with broken backspace
text = input()

# Fix the backspace issue and print the corrected text
corrected_text = fix_backspace(text)
print(corrected_text)
