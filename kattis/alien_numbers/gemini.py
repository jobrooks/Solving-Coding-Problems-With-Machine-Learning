# Difficulty: 2.8
# Justification: 
# Result: passed
# Tests passed: 3/3
# Error: none
# Response: 
def convert_number(alien_number, source_language, target_language):
  """
  Converts a number from one alien numeral system to another.

  Args:
      alien_number: The number in the source language (string).
      source_language: The list of digits in the source language (ordered by value).
      target_language: The list of digits in the target language (ordered by value).

  Returns:
      The converted number in the target language (string).
  """
  # Convert the /alien number to decimal
  decimal_value = 0
  base = len(source_language)
  for i, digit in enumerate(alien_number[::-1]):
    decimal_value += source_language.index(digit) * (base**i)

  # Convert the decimal value to the target language
  target_number = ""
  while decimal_value > 0:
    remainder = decimal_value % len(target_language)
    target_number = target_language[remainder] + target_number
    decimal_value //= len(target_language)

  return target_number

def main():
  """
  Reads input and performs alien number conversions.
  """
  num_cases = int(input())
  for case in range(1, num_cases + 1):
    alien_number, source_language, target_language = input().split()
    source_language = list(source_language)
    target_language = list(target_language)
    converted_number = convert_number(alien_number, source_language, target_language)
    print(f"Case #{case}: {converted_number}")

if __name__ == "__main__":
  main()
