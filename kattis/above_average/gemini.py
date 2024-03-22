# Difficulty: 2.3
# Justification: 
# Result: error
# Tests passed: 0/2
# Error: run-time error
# Response: 
def above_average(grades):
  """
  Calculates the percentage of students with grades above average.

  Args:
      grades: A list of integer grades (0-100).

  Returns:
      A float representing the percentage of students above average, rounded to 3 decimal places.
  """
  # Calculate the average grade
  average = sum(grades) / len(grades)

  # Count students above average
  above_count = 0
  for grade in grades:
    if grade > average:
      above_count += 1

  # Calculate and format percentage
  percentage = (above_count / len(grades)) * 100
  return round(percentage, 3)

# Read the number of test cases
num_cases = int(input())

# Loop through each test case
for _ in range(num_cases):
  # Read the number of students and their grades
  num_students = int(input())
  grades = [int(grade) for grade in input().split()]

  # Calculate and print the percentage above average
  above_avg_percent = above_average(grades)
  print(f"{above_avg_percent:.3f}")
