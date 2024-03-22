# 3.6 accepted 6/6
while True:
    try:
        a, b, c = map(int, input().split())
        quotient = a // b
        remainder = a % b
        result = []
        for i in range(c):
            result.append(str((remainder * 10) // b))
            remainder = (remainder * 10) % b
        print(str(quotient) + "." + "".join(result))
    except EOFError:
        break
