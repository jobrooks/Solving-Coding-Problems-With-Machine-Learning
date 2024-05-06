import sys

N = 0
Q = 0
boxes = []
a = []
b = []
queries = []

def initialize():
  global N, Q, boxes, a, b, queries
  N, Q = [int(x) for x in sys.stdin.read().split()]
  boxes = [[] for _ in range(N)]
  a = [0] * N
  b = [0] * N
  queries = [[] for _ in range(Q)]

def read_queries():
  for i in range(Q):
    query = sys.stdin.read().split()
    query_type = int(query[0])
    if query_type == 1:
      u = int(query[1])
      v = int(query[2])
      queries[i] = [u, v]
    elif query_type == 2:
      queries[i] = [query_type]

def compute_a_and_b():
  for i in range(Q):
    query = queries[i]
    if query[0] == 1:
      u = query[1] - 1
      v = query[2] - 1
      for j in range(u, v + 1):
        a[j] += 1
        b[j] += a[j]

def compute_e_a():
  e_a = 0
  for i in range(N):
    e_a += a[i] ** 2
  return e_a

def compute_answer():
  for i in range(Q):
    query = queries[i]
    if query[0] == 2:
      e_a = compute_e_a()
      print((e_a % (10 ** 9 + 7)) * pow(b[N - 1], -1, 10 ** 9 + 7) % (10 ** 9 + 7))

def main():
  initialize()
  read_queries()
  compute_a_and_b()
  compute_answer()

main()