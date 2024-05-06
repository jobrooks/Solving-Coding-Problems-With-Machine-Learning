mod = int(1e9) + 7

def swap(arr, i, j):
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

def flip(arr, i):
    arr[i - 1] = '*' if arr[i - 1] == '+' else '+'

ops = {'+': lambda x, y: (x + y) % mod, '*': lambda x, y: (x * y) % mod}

def evaluate(arr):
    stack = []
    for x in arr:
        if x.isdigit():
            stack.append(int(x))
        else:
            y = stack.pop()
            x = stack.pop()
            stack.append(ops[x](x, y))
    return stack[0]

arr = input()
print(evaluate(arr))
for _ in range(int(input())):
    query = input()
    if query[0] == 's':
        i, j = map(int, query[2:].split(' '))
        swap(arr, i, j)
    elif query[0] == 'f':
        i = int(query[2:])
        flip(arr, i)
    else:
        for i in range(1, len(arr) - 1, 2):
            flip(arr, i)
    print(evaluate(arr))