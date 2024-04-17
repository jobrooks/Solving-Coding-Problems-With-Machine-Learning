cars = {}
events = {}

def car_cost(car, distance):
  return cars[car][2] + distance * cars[car][3]

def check_consistency(spy):
  if len(events[spy]) % 2 != 0:
    return False

  for i in range(len(events[spy]) // 2):
    if events[spy][i][0] != 'p' or events[spy][i+1][0] != 'r':
      return False

    if events[spy][i][1] != events[spy][i+1][1]:
      return False

  return True

def calculate_cost(events, cars):
  spy_costs = {}
  for spy in events:
    if not check_consistency(spy):
      spy_costs[spy] = "INCONSISTENT"
      continue

    cost = 0
    for i in range(len(events[spy]) // 2):
      car = events[spy][i][1]
      distance = events[spy][i+1][1]
      cost += car_cost(car, distance)

      for j in range(i+1, len(events[spy])):
        if events[spy][j][1] == car:
          cost += car_cost(car, 0.01 * cars[car][1] * int(events[spy][j][1]))
          break
    spy_costs[spy] = cost

  return spy_costs

for test_case in range(int(input())):
  n, m = map(int, input().split())
  for i in range(n):
    name, price, pickup_cost, cost_per_km = input().split()
    cars[name] = [int(price), int(pickup_cost), int(cost_per_km)]
  for i in range(m):
    t, spy, event_type = input().split()
    if event_type == 'p' or event_type == 'r':
      car = input()
      if spy not in events:
        events[spy] = []
      events[spy].append([event_type, car, t])
    elif event_type == 'a':
      severity = input()
      if spy not in events:
        events[spy] = []
      events[spy].append(['a', int(severity), t])

  for spy, costs in sorted(calculate_cost(events, cars).items()):
    print(spy, costs)