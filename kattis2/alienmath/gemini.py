def alien_to_decimal(base, digits, number):
    """
    Converts an alien number to a decimal number.

    Args:
        base: The base of the alien number system.
        digits: A list of the digits in the alien number system.
        number: The alien number to convert.

    Returns:
        The decimal value of the alien number.
    """
    decimal_value = 0
    for i in range(len(number)):
        digit_value = digits.index(number[i])
        decimal_value += digit_value * (base ** (len(number) - i - 1))
    return decimal_value

if __name__ == "__main__":
    base = int(input())
    digits = input().split()
    number = input()
    decimal_value = alien_to_decimal(base, digits, number)
    print(decimal_value)