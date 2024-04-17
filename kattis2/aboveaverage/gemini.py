import math

def main():
  # Read the number of test cases
  C = int(input())

  # Loop over the test cases
  for i in range(C):
    # Read the number of students
    N = int(input())

    # Read the list of grades
    grades = list(map(int, input().split()))

    # Calculate the average grade
    average = sum(grades) / N

    # Count the number of students above average
    above_average = 0
    for grade in grades:
      if grade > average:
        above_average += 1

    # Calculate the percentage of students above average
    percentage_above_average = above_average / N * 100

    # Round the percentage to 3 decimal places
    percentage_above_average = math.ceil(percentage_above_average * 1000) / 1000

    # Print the percentage
    print(f'{percentage_above_average:.3f}%')

if __name__ == "__main__":
  main()