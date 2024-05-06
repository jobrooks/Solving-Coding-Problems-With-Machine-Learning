import re

def is_valid_unary(num):
    return num.count('1') == len(num)

def is_valid_base(num, base):
    if base == 1:
        return is_valid_unary(num)
    else:
        try:
            int(num, base)
            return True
        except ValueError:
            return False

def is_valid_expression(expr, base):
    x, op, y, eq, z = expr.split()
    return is_valid_base(x, base) and is_valid_base(y, base) and is_valid_base(z, base)

def get_valid_bases(expr):
    valid_bases = []
    for base in range(1, 37):
        if is_valid_expression(expr, base):
            valid_bases.append(base)
    return valid_bases

def main():
    num_tests = int(input())
    for i in range(num_tests):
        expr = input()
        valid_bases = get_valid_bases(expr)
        if not valid_bases:
            print("invalid")
        else:
            # convert bases to alphabetic characters
            valid_bases = [chr(ord('a') + base - 10) if base > 9 else str(base) for base in valid_bases[::-1]]
            print(''.join(valid_bases))

if __name__ == "__main__":
    main()