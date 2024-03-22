# 2.4 wrong answer 0/2

# read the number of test cases
C = int(input())

for _ in range(C):
    # read the grades
    grades = list(map(int, input().split()))

    # calculate the average
    avg = sum(grades[1:]) / grades[0]

    # count the number of grades above average
    count = sum(1 for grade in grades[1:] if grade > avg)

    # calculate the percentage of grades above average
    percent = count / (grades[0] - 1) * 100

    # print the result with 3 decimal places
    print(f"{percent:.3f}%")
