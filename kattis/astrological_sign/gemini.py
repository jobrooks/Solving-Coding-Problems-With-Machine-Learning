# Difficulty: 2.3
# Justification: 
# Result: Run-Time Error
# Tests passed: 0/15
# Error: run-time error
# Response: 
def get_zodiac_sign(date_str):
  """
  Calculates the zodiac sign based on a given date string.

  Args:
      date_str: The date in "mm/dd" format (string).

  Returns:
      The corresponding zodiac sign (string).
  """

  # Extract month and day from the date string
  month, day = map(int, date_str.split("/"))

  # Define zodiac sign ranges (month, start day, end day)
  signs = [
      ("Capricorn", 12, 22, 1, 19),
      ("Aquarius", 1, 20, 2, 18),
      ("Pisces", 2, 19, 3, 20),
      ("Aries", 3, 21, 4, 19),
      ("Taurus", 4, 20, 5, 20),
      ("Gemini", 5, 21, 6, 20),
      ("Cancer", 6, 21, 7, 22),
      ("Leo", 7, 23, 8, 22),
      ("Virgo", 8, 23, 9, 22),
      ("Libra", 9, 23, 10, 22),
      ("Scorpio", 10, 23, 11, 21),
      ("Sagittarius", 11, 22, 12, 21),
  ]

  # Find the zodiac sign based on month and day
  for sign, start_month, start_day, end_month, end_day in signs:
    if (month == start_month and day >= start_day) or \
       (month == end_month and day <= end_day):
      return sign

  # Handle edge cases (dates spanning across year boundary)
  if month == 12 and day > 21:
    return signs[0][0]  # Capricorn for December dates after 21st
  elif month == 1 and day <= 19:
    return signs[-1][0]  # Aquarius for January dates before 20th

  # Invalid date format (should not reach here)
  return "Invalid date format"

# Read input date
date_str = input("Enter date (mm/dd): ")

# Calculate and print the zodiac sign
zodiac_sign = get_zodiac_sign(date_str)
print(zodiac_sign)
