import re
import sys

def is_valid(expr, base):
  """Returns True if the expression is valid in the given base."""

  # Check if all the operands are valid in the given base.
  for operand in re.findall(r'[0-9a-z]+', expr):
    if int(operand, base) < 1 or int(operand, base) >= 2**32:
      return False

  # Check if the expression is true.
  result = eval(expr.replace(' ', ''), {}, {'0': 0})
  if result < 1 or result >= 2**32:
    return False

  return True

def main():
  """Reads the input and prints the results."""

  # Read the number of expressions.
  n = int(sys.stdin.readline())

  # Read the expressions.
  expressions = []
  for i in range(n):
    expressions.append(sys.stdin.readline().strip())

  # Check if each expression is valid in bases 1-36.
  for expr in expressions:
    valid_bases = []
    for base in range(1, 37):
      if is_valid(expr, base):
        valid_bases.append(base)

    # Print the valid bases or the word "invalid".
    if valid_bases:
      print(' '.join(map(str, valid_bases)))
    else:
      print('invalid')

if __name__ == "__main__":
  main()