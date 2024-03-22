# 1.3 accepted 200/200
import sys

def whoWins(n: int) -> str:
    return "Alice" if n % 2 == 1 else "Bob"


for line in sys.stdin.readlines():
  print(whoWins(int(line)))