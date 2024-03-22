# 2.0 run-time error 0/4

def sexagesimal_to_decimal(s):
    digits = s.split(',')
    decimal = 0
    for i in range(len(digits)):
        decimal += int(digits[i]) * 60**(len(digits)-1-i)
    return decimal

# main program
n = int(input())
for i in range(n):
    s = input().strip()
    print(sexagesimal_to_decimal(s))
