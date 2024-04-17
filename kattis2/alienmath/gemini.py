def alien_to_decimal(base, digits, number):
  """Converts an alien number to decimal.

  Args:
    base: The base of the alien number system.
    digits: A list of strings representing the digits of the alien number system.
    number: The alien number to convert.

  Returns:
    The decimal value of the alien number.
  """

  # Create a dictionary of alien digits to their decimal values.
  digit_values = {}
  for i in range(base):
    digit_values[digits[i]] = i

  # Convert the alien number to a list of decimal digits.
  decimal_digits = []
  for digit in number:
    decimal_digits.append(digit_values[digit])

  # Convert the list of decimal digits to a decimal number.
  decimal_number = 0
  for i in range(len(decimal_digits)):
    decimal_number += decimal_digits[i] * (base ** (len(decimal_digits) - i - 1))

  return decimal_number


def main():
  # Read the input.
  base = int(input())
  digits = input().split()
  number = input()

  # Convert the alien number to decimal.
  decimal_number = alien_to_decimal(base, digits, number)

  # Print the result.
  print(decimal_number)


if __name__ == "__main__":
  main()