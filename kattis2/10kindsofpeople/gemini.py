def is_possible(map, r1, c1, r2, c2, binary):
  if binary:
    if map[r1][c1] == '0' and map[r2][c2] == '0':
      return True
    else:
      return False
  else:
    if map[r1][c1] == '1' and map[r2][c2] == '1':
      return True
    else:
      return False

def main():
  r, c = map(int, input().split())
  map = [input() for _ in range(r)]
  n = int(input())
  for _ in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    if is_possible(map, r1 - 1, c1 - 1, r2 - 1, c2 - 1, True):
      print('binary')
    elif is_possible(map, r1 - 1, c1 - 1, r2 - 1, c2 - 1, False):
      print('decimal')
    else:
      print('neither')

if __name__ == "__main__":
  main()