def alien_convert(alien_number, source_language, target_language):
  """Converts an alien number from one language to another.

  Args:
    alien_number: The alien number to convert.
    source_language: The language the alien number is currently in.
    target_language: The language to convert the alien number to.

  Returns:
    The alien number in the target language.
  """

  # Create a dictionary of the source language digits to their values.
  source_language_digits = {}
  for i, digit in enumerate(source_language):
    source_language_digits[digit] = i

  # Create a dictionary of the target language digits to their values.
  target_language_digits = {}
  for i, digit in enumerate(target_language):
    target_language_digits[digit] = i

  # Convert the alien number to a decimal number.
  decimal_number = 0
  for digit in alien_number:
    decimal_number *= len(source_language)
    decimal_number += source_language_digits[digit]

  # Convert the decimal number to the target language.
  target_language_number = ""
  while decimal_number > 0:
    remainder = decimal_number % len(target_language)
    target_language_number = target_language[remainder] + target_language_number
    decimal_number //= len(target_language)

  return target_language_number


def main():
  """Gets input and prints the converted alien numbers."""

  # Get the number of test cases.
  t = int(input())

  # Loop over the test cases.
  for i in range(t):
    # Get the input for the test case.
    alien_number, source_language, target_language = input().split()

    # Convert the alien number from the source language to the target language.
    converted_number = alien_convert(alien_number, source_language, target_language)

    # Print the converted number.
    print("Case #{}: {}".format(i + 1, converted_number))


if __name__ == "__main__":
  main()