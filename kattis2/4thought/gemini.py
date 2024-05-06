# 3.0 wrong answer 1/3
def solve(n):
    """Given an integer n as input, will produce a mathematical expression whose solution is n.
    The solution is restricted to using exactly four 4’s and exactly three of the binary operations
    selected from the set { *, +, -, /} . The number 4 is the ONLY number you can use. You are not
    allowed to concatenate fours to generate other numbers, such as 44 or 444.
    For example given n=0, a solution is 4 * 4 - 4 * 4 = 0. Given n=7, a solution is 4 + 4 - 4~ /~ 4 = 7.
    Division is considered truncating integer division, so that 1/4 is 0 (instead of 0.25).
    Assume the usual precedence of operations so that 4 + 4 * 4 = 20, not 32. Not all integer inputs
    have solutions using four 4’s with the aforementioned restrictions (consider n=11).
    """
    if (n % 4 == 0):
        return "4 * 4 - 4 * 4 = " + str(n)
    elif ((n + 4) % 4 == 0):
        return "4 + 4 - 4 / 4 = " + str(n)
    elif((n - 4) % 4 == 0):
        return "4 - 4 + 4 * 4 = " + str(n)
    elif((n + 8) % 4 == 0):
        return "4 / 4 + 4 * 4 = " + str(n)
    elif((n - 8) % 4 == 0):
        return "4 * 4 - 4 - 4 = " + str(n)
    elif((n + 12) % 4 == 0):
        return "4 + 4 + 4 + 4 = " + str(n)
    else:
        return "no solution"

num_tests = int(input())
for i in range(num_tests):
    n = int(input())
    print(solve(n))