#!/bin/python

import sys
from collections import deque

def main():
    r, c = map(int, input().split())
    orig = [[0] * c for _ in range(r)]
    pref = [[0] * c for _ in range(r)]
    for i in range(r):
        orig[i] = list(map(int, input().split()))
    for i in range(r):
        pref[i] = list(map(int, input().split()))
    
    swaps = []
    for i in range(r):
        for j in range(c):
            orig[i][pref[i].index(orig[i][j])] = pref[i][j]
    
    for i in range(r):
        for j in range(c):
            if orig[i][j] != pref[i][j]:
                for k in range(j+1, c):
                    if orig[i][k] == pref[i][j]:
                        swaps.append((i+1, j+1, i+1, k+1))
                        orig[i][j], orig[i][k] = orig[i][k], orig[i][j]
                        break
    
    print(len(swaps))
    for swap in swaps:
        print(*swap)

if __name__ == "__main__":
    main()