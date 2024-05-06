# 2.3 Error 1/2
num_cases = int(input())

for i in range(num_cases):
    num_students = int(input())
    grades = [int(x) for x in input().split()]
    avg = sum(grades) / num_students
    above_avg = len([grade for grade in grades if grade > avg])
    print("{:.3f}%".format(above_avg / num_students * 100))