# 4.4 Wrong Answer 0/12
def find_rising_falling(n):
    digits = list(map(int, str(n)))  # Convert n to a list of digits

    # Find the index i such that digits[i] > digits[i+1]
    i = len(digits) - 2
    while i >= 0 and digits[i] <= digits[i+1]:
        i -= 1

    # If no such index is found, n is already a rising and falling number
    if i == -1:
        return n

    # Find the index j such that digits[j] < digits[j+1], starting from the end
    j = len(digits) - 1
    while j > i and digits[j] >= digits[j-1]:
        j -= 1

    # Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the digits after index i
    digits[i+1:] = reversed(digits[i+1:])

    # Convert the list of digits back to an integer
    return int(''.join(map(str, digits)))


# Main function to read input and output results
if __name__ == '__main__':
    t = int(input())  # Read the number of test cases

    for i in range(t):
        n = int(input())  # Read the input number for this test case
        print(find_rising_falling(n))  # Output the largest rising and falling number less than or equal to n
# 
