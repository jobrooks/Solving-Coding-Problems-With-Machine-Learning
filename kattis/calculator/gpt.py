# 3.2 run-time error 0/2

import sys

# Define a function to convert infix to postfix notation
def infix_to_postfix(expr):
    # Define operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    # Initialize empty stack and output list
    stack = []
    output = []

    # Loop through each token in the expression
    for token in expr.split():
        # If token is a number, add it to the output list
        if token.isdigit():
            output.append(int(token))
        # If token is an operator, pop operators from stack and add to output list
        # until stack is empty or top operator has lower precedence than current operator
        elif token in precedence:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        # If token is a left parenthesis, push to stack
        elif token == "(":
            stack.append(token)
        # If token is a right parenthesis, pop operators from stack and add to output list
        # until left parenthesis is reached, then discard left parenthesis
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()

    # Pop any remaining operators from stack and add to output list
    while stack:
        output.append(stack.pop())

    return output

# Define a function to evaluate postfix notation
def evaluate_postfix(expr):
    # Initialize stack
    stack = []

    # Loop through each token in the postfix expression
    for token in expr:
        # If token is a number, push to stack
        if isinstance(token, int):
            stack.append(token)
        # If token is an operator, pop two numbers from stack, apply operator,
        # and push result to stack
        elif token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)

    return stack[0]

# Loop through each line of input
for line in sys.stdin:
    # Convert infix expression to postfix notation
    postfix_expr = infix_to_postfix(line.strip())

    # Evaluate postfix expression and print result with two digits of precision
    result = evaluate_postfix(postfix_expr)
    print("{:.2f}".format(result))
