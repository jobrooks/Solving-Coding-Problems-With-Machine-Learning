# Difficulty: 2.6
# Justification: 
# Result: failed
# Tests passed: 0/7
# Error: none
# Response: 
# Define the substitution dictionary
substitution = {
    'A': '@', 'B': '8', 'C': '(', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': '#', 'I': '!',
    'J': 'J', 'K': 'K', 'L': '1', 'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'R',
    'S': '$', 'T': '7', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '2',
    'a': '@', 'b': '8', 'c': '(', 'd': 'D', 'e': '3', 'f': 'F', 'g': '6', 'h': '#', 'i': '!',
    'j': 'J', 'k': 'K', 'l': '1', 'm': 'M', 'n': 'N', 'o': '0', 'p': 'P', 'q': 'Q', 'r': 'R',
    's': '$', 't': '7', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': '2'
}

def decrypt_message(message):
  """Decrypts a message using the substitution cipher."""
  decrypted_message = ""
  for char in message:
    if char.isalpha():
      decrypted_message += substitution[char]
    else:
      decrypted_message += char
  return decrypted_message

# Get the encrypted message
encrypted_message = input("Enter the encrypted message: ")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message)

# Print the decrypted message
print("Decrypted message:", decrypted_message)
