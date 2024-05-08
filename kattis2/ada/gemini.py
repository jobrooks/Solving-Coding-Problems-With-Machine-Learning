# 2.4 Error 1/17
import sys

def main():
    # read input
    n = int(input())
    v = [int(x) for x in input().split()]

    # compute differences
    d = []
    for i in range(1, n):
        d.append(v[i] - v[i-1])

    # compute degree of polynomial
    degree = 1
    while degree < n and all(d[i] == d[i-1] for i in range(1, degree)):
        degree += 1

    # compute next value
    v_next = v[-1] + d[-1]

    # print output
    print(degree, v_next)

if __name__ == '__main__':
    main()