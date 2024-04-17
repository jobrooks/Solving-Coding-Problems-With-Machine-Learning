# Open the input file and read each line
with open("input.txt", "r") as f:
    lines = f.readlines()

# Initialise the dictionary to store the word-number pairs
word_values = {}

# Process each line in the input file
for line in lines:
    # Split the line into tokens
    tokens = line.split()

    # Check if the command is a definition
    if tokens[0] == "def":
        # Get the variable name and value
        variable = tokens[1]
        value = int(tokens[2])

        # Update the dictionary with the new value
        word_values[variable] = value

    # Check if the command is a calculation
    elif tokens[0] == "calc":
        # Initialise the result to 0
        result = 0

        # Iterate over the tokens in the calculation
        for token in tokens[1:]:
            # Check if the token is a variable or an operator
            if token in word_values:
                # If it's a variable, add its value to the result
                result += word_values[token]
            elif token in "+-":
                # If it's an operator, use it to update the result
                operator = token
            else:
                # If it's not a variable or an operator, the calculation is invalid
                result = "unknown"
                break

        # Check if the result is valid
        if result != "unknown":
            # Print the result
            print(result)

    # Check if the command is a clear
    elif tokens[0] == "clear":
        # Clear the dictionary
        word_values.clear()