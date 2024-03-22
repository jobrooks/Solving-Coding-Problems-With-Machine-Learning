# 1.5 wrong answer 0/37

n = int(input())
s = input()

# initialize a stack to keep track of the opening brackets
stack = []

# loop through each bracket in the sequence
for bracket in s:
    if bracket in '([{':
        # if the bracket is an opening bracket, push it onto the stack
        stack.append(bracket)
    else:
        # if the bracket is a closing bracket, check if it matches the top of the stack
        if not stack:
            # if the stack is empty, the sequence is invalid
            print("NO")
            break
        top = stack.pop()
        if (bracket == ')' and top != '(') or (bracket == ']' and top != '[') or (bracket == '}' and top != '{'):
            # if the closing bracket does not match the opening bracket, the sequence is invalid
            print("NO")
            break
else:
    # if the loop completes without any breaks, the sequence is valid
    if not stack:
        print("YES")
    else:
        print("NO")