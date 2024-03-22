# 1.7 accepted 7/7

import sys

# Define a dictionary of replacements for each character
replacements = {
    'a': '@',
    'b': '8',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\/[]',
    'n': '[]\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': "']['",
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '}{',
    'y': '`/',
    'z': '2'
}

# Read in the input string
input_string = sys.stdin.readline().strip()

# Loop through each character in the input string and replace it if necessary
output_string = ""
for c in input_string:
    if c.lower() in replacements:
        output_string += replacements[c.lower()]
    else:
        output_string += c

# Output the result
print(output_string)
