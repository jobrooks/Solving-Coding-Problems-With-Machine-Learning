def convert_to_dec(alien_number, source_language):
  """Converts an alien number to a decimal number.

  Args:
    alien_number: The alien number to convert.
    source_language: The source language of the alien number.

  Returns:
    The decimal equivalent of the alien number.
  """

  dec_result = 0
  for i, digit in enumerate(alien_number):
    dec_result += source_language.index(digit) * (len(source_language) ** i)
  return dec_result


def convert_from_to(dec_number, source_language, target_language):
  """Converts a decimal number from one language to another.

  Args:
    dec_number: The decimal number to convert.
    source_language: The source language of the decimal number.
    target_language: The target language of the decimal number.

  Returns:
    The alien number in the target language.
  """

  result = []
  while dec_number > 0:
    result.append(target_language[dec_number % len(target_language)])
    dec_number //= len(target_language)
  return ''.join(result[::-1])


def main():
  """Gets the number of test cases and processes each test case."""

  num_test_cases = int(input())

  for test_case in range(1, num_test_cases + 1):
    alien_number, source_language, target_language = input().split()

    dec_number = convert_to_dec(alien_number, source_language)
    result = convert_from_to(dec_number, source_language, target_language)

    print("Case #{}: {}".format(test_case, result))


if __name__ == "__main__":
  main()