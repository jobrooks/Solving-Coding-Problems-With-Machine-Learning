# Difficulty: 1.2
# Justification: 
# Result: wrong answer
# Tests passed: 0/16
# Error: none
# Response: 
# Get the input line
input_line = input("Enter two whole numbers separated by a space: ")

# Split the line into individual numbers
num1, num2 = map(int, input_line.split())

# Calculate the sum
sum = num1 + num2

# Print the sum
print("The sum of", num1, "and", num2, "is", sum)
