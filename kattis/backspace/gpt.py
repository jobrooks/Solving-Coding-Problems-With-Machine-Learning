# 2.2 accepted 25/25

string = input()
stack = []

for char in string:
    if char == '<':
        stack.pop()
    else:
        stack.append(char)

print(''.join(stack))
