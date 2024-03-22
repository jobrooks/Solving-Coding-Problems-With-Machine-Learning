# 2.3 wrong answer 0/12

def main():
    a, b, c = map(int, input().split())
    desired_order = input().strip()
    numbers = [a, b, c]
    ordered_numbers = [0] * 3
    for i, letter in enumerate(desired_order):
        if letter == 'A':
            ordered_numbers[i] = min(numbers)
        elif letter == 'B':
            ordered_numbers[i] = sorted(numbers)[1]
        elif letter == 'C':
            ordered_numbers[i] = max(numbers)
        numbers.remove(ordered_numbers[i])
    print(*ordered_numbers)

if __name__ == "__main__":
    main()
