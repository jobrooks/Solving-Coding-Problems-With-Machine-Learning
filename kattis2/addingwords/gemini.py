import sys

# Initialize the dictionary of variables to their values
variables = {}

# Read the input commands
for line in sys.stdin:
    # Split the command into tokens
    tokens = line.split()

    # If the command is a definition, add the variable to the dictionary
    if tokens[0] == "def":
        variables[tokens[1]] = int(tokens[2])

    # If the command is a calculation, evaluate the calculation and print the result
    elif tokens[0] == "calc":
        result = 0
        for token in tokens[1:-1]:
            if token in variables:
                result += variables[token]
            else:
                result = "unknown"
                break
        print(result)

    # If the command is a clear, clear the dictionary of variables
    elif tokens[0] == "clear":
        variables.clear()