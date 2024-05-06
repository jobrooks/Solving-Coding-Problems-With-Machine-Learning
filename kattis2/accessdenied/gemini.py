# 4.1 Error 0/92
import time
import sys

def CheckPassword(pwd1, pwd2):
  if len(pwd1) != len(pwd2):
    return False
  for i in range(len(pwd1)):
    if pwd1[i] != pwd2[i]:
      return False
  return True

PWD_LEN = 20
MIN_PWD_LEN = 1

def get_response(sent):
  sys.stdout.buffer.write(sent.encode())
  sys.stdout.flush()
  ret = input()
  if ret == "ACCESS DENIED":
    return int(ret[len("ACCESS DENIED"): ret.find(" ")])
  elif "ACCESS GRANTED" in ret:
    return "ACCESS GRANTED"

if __name__ == "__main__":
  low = 0
  high = 26 + 10
  times = [0] * (26 + 10)
  best = 0
  for i in range(2500):
    mid = (low + high) // 2
    guess = chr(ord('a') + mid)
    times[mid] = get_response(guess)
    if times[mid] == "ACCESS GRANTED":
      break
    if times[mid] < 42:
      high = mid - 1
    else:
      low = mid + 1
      best = guess
  left = list(range(ord('a'), ord(best) + 1))
  right = list(range(ord(best), ord('z') + 1))
  times = [0] * (26 + 10)
  for i in left:
    guess = chr(i) + "*"
    times[i-ord('a')] = get_response(guess)
  for i in right:
    guess = "*" + chr(i)
    times[i-ord('a')] = get_response(guess)
  best = -1
  for i in range(26 + 10):
    if times[i] < 42:
      best = i
  if best == -1:
    for i in left:
      for j in range(10):
        times[10 + i - ord('a')] = get_response(chr(i) + str(j))
  for i in range(26 + 10):
    if times[i] < 42:
      best = chr(ord('a') + i)
      break
  times = [0] * (26 + 10)
  for i in range(2500):
    times[ord(best)-ord('a')] = get_response(chr(ord('a') + i) + best)
    if times[ord(best)-ord('a')] < 42:
      best = best + chr(ord('a') + i)
      break
  if CheckPassword(get_response(best), best):
    print("The password is", best)