# Difficulty: 2.5
# Result: Run-time Error
# Tests passed: 0/2
# Error: run-time
# Response: 
def translate_message(dictionary, message):
  """
  Translates a message from a foreign language to English using a dictionary.

  Args:
      dictionary: A dictionary mapping foreign words to English words.
      message: A list of foreign language words in the message.

  Returns:
      A list of translated English words for the message.
  """

  # Create a dictionary for faster lookups
  foreign_to_english = {word: english for english, word in dictionary}

  # Translate each word in the message
  translated_message = []
  for word in message:
    translation = foreign_to_english.get(word, "eh")  # "eh" for unknown words
    translated_message.append(translation)

  return translated_message

# Read dictionary entries
dictionary = []
while True:
  line = input().strip()
  if not line:
    break
  english, foreign = line.split()
  dictionary.append((english, foreign))

# Read message lines
message = []
while True:
  line = input().strip()
  if not line:
    break
  message.append(line)

# Translate the message and print results
translated_message = translate_message(dictionary, message)
for word in translated_message:
  print(word)
