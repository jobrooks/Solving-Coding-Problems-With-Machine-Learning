# # 3.3 run-time error 0/3

import itertools

# Define the set of binary operations
operations = ['*', '+', '-', '/']

# Define a function to evaluate a given expression
def evaluate_expression(expr):
    try:
        return eval(expr)
    except ZeroDivisionError:
        return None

# Define a function to generate all possible expressions using four 4's
def generate_expressions():
    expressions = []
    for ops in itertools.product(operations, repeat=3):
        for nums in itertools.permutations(['4', '4', '4', '4'], 4):
            expr = nums[0] + ops[0] + nums[1] + ops[1] + nums[2] + ops[2] + nums[3]
            result = evaluate_expression(expr)
            if result is not None and result == i:
                expressions.append(expr)
    return expressions

# Read the number of test cases
m = int(input())

# Iterate over each test case
for _ in range(m):
    # Read the target number
    n = int(input())
    
    # Generate all possible expressions
    expressions = generate_expressions()
    
    # Print the first expression that evaluates to the target number, or 'no solution' if none exist
    if len(expressions) > 0:
        print(expressions[0] + ' = ' + str(n))
    else:
        print('no solution')
