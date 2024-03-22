# Difficulty: 4.1
# Justification: 
# Result: Run-Time Error
# Tests passed: 0/11
# Error: Run-Time Error
# Response: 
class WordAdder:
  """
  A class to represent a word adder program for psychologist experiments.
  """
  def __init__(self):
    self.definitions = {}  # Dictionary to store word-number definitions

  def process_command(self, command):
    """
    Processes a single command (definition, calculation, or clear).
    """
    words = command.split()
    if words[0] == "def":
      self.define(words[1], int(words[2]))
    elif words[0] == "calc":
      self.calculate(words[1:])
    elif words[0] == "clear":
      self.definitions = {}
    else:
      print("Unknown command:", command)

  def define(self, word, value):
    """
    Defines a word to represent a specific number.
    """
    self.definitions[word] = value

  def calculate(self, expression):
    """
    Calculates the value of an expression using defined words.
    """
    result = 0
    unknown = False
    for word in expression[:-1]:  # Skip the "=" sign
      if word in self.definitions:
        result += self.definitions[word]
      else:
        unknown = True
        break
    operator = expression[-2]  # Get the last operator (+ or -)
    if operator == "+":
      result += int(expression[-1])  # Add the last number
    elif operator == "-":
      result -= int(expression[-1])  # Subtract the last number
    else:
      print("Unknown operator:", operator)

    if unknown:
      print("unknown")
    else:
      print(result)

def main():
  """
  Reads input commands and processes them using the WordAdder class.
  """
  word_adder = WordAdder()
  while True:
    line = input().strip()
    if not line:
      break
    word_adder.process_command(line)

if __name__ == "__main__":
  main()
