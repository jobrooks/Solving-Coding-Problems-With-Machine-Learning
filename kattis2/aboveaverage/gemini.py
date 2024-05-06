# 2.3 Error 1/2
import statistics

for _ in range(int(input())):
    n = int(input())
    grades = [int(x) for x in input().split()]
    avg = statistics.mean(grades)
    above_avg = sum(1 for grade in grades if grade > avg)
    print(f"{above_avg / n * 100:.3f}%")