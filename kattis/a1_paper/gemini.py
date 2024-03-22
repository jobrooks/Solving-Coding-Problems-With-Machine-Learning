# Difficulty: 4.3
# Justification: 
# Result: failed
# Tests passed: 0/13
# Error: none
# Response: 
import math

def area_of_paper(n):
  """Calculates the area of an A-size paper."""
  return 2 ** ((n - 4) / 4)

def get_tape_length(n, papers):
  """Calculates the minimum tape length needed to make an A1 paper."""
  required_area = area_of_paper(1)
  total_area = 0
  tape_length = 0
  for size, count in enumerate(papers, start=2):
    area = area_of_paper(size)
    total_area += area * count
    tape_length += area * (count - 1) * 2 ** (- (size - 3) / 4)
    if total_area >= required_area:
      return tape_length
  return "impossible"

def main():
  """Reads input, calculates tape length, and prints output."""
  n = int(input())
  papers = [int(x) for x in input().split()]
  tape_length = get_tape_length(n, papers)
  print(tape_length if tape_length != "impossible" else "impossible")

if __name__ == "__main__":
  main()
