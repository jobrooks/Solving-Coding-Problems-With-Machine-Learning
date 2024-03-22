# 1.3 accepted 12/12
import sys

def restore_R2(R1, S):
    return 2 * S - R1

#R1, S = map(int, input("Enter two integers R1 and S: ").split())
#R2 = restore_R2(R1, S)
#print("R2 is", R2)



for line in sys.stdin.readlines():
  R1, S = map(int, line.split())
  R2 = restore_R2(R1, S)
  print(R2)