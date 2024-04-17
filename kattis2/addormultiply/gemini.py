base = 10 ** 9 + 7

def main():
    n, m = map(int, input().split())
    s = input()
    # Store the number blocks in a list
    numbers = []
    for i in range(0, len(s), 2):
        numbers.append(int(s[i]))
    # Store the operator blocks in a list
    operators = []
    for i in range(1, len(s), 2):
        operators.append(s[i])
    # Evaluate the initial expression
    result = evaluate(numbers, operators)
    print(result)
    # Process the queries
    for i in range(m):
        query = input()
        if query.startswith("s"):
            # Swap two numbers
            a, b = map(int, query[2:].split())
            numbers[a - 1], numbers[b - 1] = numbers[b - 1], numbers[a - 1]
        elif query.startswith("f"):
            # Flip an operator
            a = int(query[2:]) - 1
            operators[a] = "*" if operators[a] == "+" else "+"
        else:
            # Flip all operators
            for i in range(len(operators)):
                operators[i] = "*" if operators[i] == "+" else "+"
        # Evaluate the updated expression
        result = evaluate(numbers, operators)
        print(result)

def evaluate(numbers, operators):
    # Initialize the stack with the first number
    stack = [numbers[0]]
    # Iterate over the remaining numbers and operators
    for i in range(len(numbers) - 1):
        if operators[i] == "+":
            # Pop the top two numbers from the stack and add them
            a = stack.pop()
            b = stack.pop()
            stack.append((a + b) % base)
        else:
            # Pop the top two numbers from the stack and multiply them
            a = stack.pop()
            b = stack.pop()
            stack.append((a * b) % base)
    # Return the top of the stack as the result
    return stack[0]

if __name__ == "__main__":
    main()