# 3.0 Error 1/3
def main():
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        if n == 4 * 4 * 4 - 4:
            print("4 * 4 * 4 - 4")
        elif n == 4 * 4 * 4 + 4:
            print("4 * 4 * 4 + 4")
        elif n == 4 * 4 + 4 * 4:
            print("4 * 4 + 4 * 4")
        elif n == 44 - 4 / 4:
            print("44 - 4 / 4")
        elif n == 44 + 4 / 4:
            print("44 + 4 / 4")
        elif n == 44 - 4 * 4:
            print("44 - 4 * 4")
        elif n == 44 + 4 * 4:
            print("44 + 4 * 4")
        elif n == 4 + 44 / 4:
            print("4 + 44 / 4")
        elif n == 4 - 44 / 4:
            print("4 - 44 / 4")
        elif n == 4 + 4 + 4 * 4:
            print("4 + 4 + 4 * 4")
        elif n == 4 + 4 - 4 * 4:
            print("4 + 4 - 4 * 4")
        elif n == 4 - 4 - 4 * 4:
            print("4 - 4 - 4 * 4")
        elif n == 4 - 4 + 4 * 4:
            print("4 - 4 + 4 * 4")
        elif n == 4 + 44 - 4:
            print("4 + 44 - 4")
        elif n == 4 + 4 - 44:
            print("4 + 4 - 44")
        elif n == 4 - 44 + 4:
            print("4 - 44 + 4")
        elif n == 4 - 4 - 44:
            print("4 - 4 - 44")
        elif n == 44 / 4 + 4:
            print("44 / 4 + 4")
        elif n == 44 / 4 - 4:
            print("44 / 4 - 4")
        else:
            print("no solution")

if __name__ == "__main__":
    main()