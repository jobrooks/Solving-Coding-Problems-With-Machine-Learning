# Difficulty: 3.1
# Justification: none
# Result: failed
# Tests passed: 0/3
# Error: none
# Response: 
import itertools

def find_expression(n):
    ops = ['+', '-', '*', '/']
    for ops_combo in itertools.combinations(ops, 3):
        for perm in itertools.permutations("4444"):
            expression = perm[0]
            for i in range(1, 4):
                expression += ops_combo[i - 1] + perm[i]
            try:
                if eval(expression) == n:
                    return f"{expression} = {n}"
            except ZeroDivisionError:
                pass
    return "no solution"

num_cases = int(input())

for _ in range(num_cases):
    n = int(input())
    expression = find_expression(n)
    print(expression)

