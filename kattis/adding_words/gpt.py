# 3.9 accepted 11/11

import sys

def parse_command(command):
    tokens = command.split()
    if tokens[0] == 'def':
        return ('def', tokens[1], int(tokens[2]))
    elif tokens[0] == 'calc':
        return ('calc', tokens[1:-1])
    elif tokens[0] == 'clear':
        return ('clear',)
    else:
        return ('unknown',)

def evaluate_expression(expression, definitions):
    result = 0
    operator = '+'
    for term in expression:
        if term == '+':
            operator = '+'
        elif term == '-':
            operator = '-'
        elif term in definitions:
            value = definitions[term]
            if operator == '+':
                result += value
            else:
                result -= value
        else:
            return 'unknown'
    return next((k for k, v in definitions.items() if v == result), 'unknown')

definitions = {}
for line in sys.stdin:
    command = parse_command(line.strip())
    if command[0] == 'def':
        definitions[command[1]] = command[2]
    elif command[0] == 'calc':
        result = evaluate_expression(command[1], definitions)
        print(' '.join(command[1]) + ' ' + '=' + ' ' + str(result))
    elif command[0] == 'clear':
        definitions = {}
