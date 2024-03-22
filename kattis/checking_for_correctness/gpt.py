# 3.8 time limit exceeded 1/2

import sys

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(a, b):
    return pow(a, b)

ops = {
    '+': add,
    '*': multiply,
    '^': power
}

for line in sys.stdin:
    a, op, b = line.strip().split()
    a = int(a)
    b = int(b)
    result = ops[op](a, b)
    last_four_digits = str(result)[-4:]
    print(int(last_four_digits))
