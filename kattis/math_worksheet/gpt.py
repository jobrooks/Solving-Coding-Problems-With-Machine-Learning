# 5.7 runtime error 0/2
import sys

def parse_math_problem(problem):
    if '+' in problem:
        x, y = map(int, problem.split('+'))
        return x + y
    elif '-' in problem:
        x, y = map(int, problem.split('-'))
        return x - y
    elif '*' in problem:
        x, y = map(int, problem.split('*'))
        return x * y

def evaluate_test_case(problems):
    max_width = 0
    results = []
    for problem in problems:
        result = parse_math_problem(problem)
        results.append(result)
        max_width = max(max_width, len(str(result)))
    return results, max_width

def print_table(results, max_width):
    cols_per_row = 50 // (max_width + 1)  # Determine how many columns fit in one row
    num_rows = len(results) // cols_per_row + (len(results) % cols_per_row != 0)
    for i in range(num_rows):
        row = results[i*cols_per_row : (i+1)*cols_per_row]
        row_str = ''.join(str(result).rjust(max_width+1) for result in row)
        print(row_str.rstrip())
    print()

while True:
    n = int(input())
    if n == 0:
        break
    problems = [input().strip() for _ in range(n)]
    results, max_width = evaluate_test_case(problems)
    print_table(results, max_width)
